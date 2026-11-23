const path = require("path");
const { Client, GatewayIntentBits } = require("discord.js");
const { Redis } = require("@upstash/redis");
const allgp = require("./all-god-packs.js");

// ================= ANTI-CRASH =================
process.on("unhandledRejection", (err) => console.error("🔥 Unhandled Rejection:", err));
process.on("uncaughtException", (err) => console.error("🔥 Uncaught Exception:", err));

// ================= VARIABLES DE ENTORNO =================
const DISCORD_TOKEN = process.env.DISCORD_TOKEN;
const LINK_REDIS_URL = process.env.LINK_REDIS_URL;
const LINK_REDIS_TOKEN = process.env.LINK_REDIS_TOKEN;

const ALL_GP_CHANNEL_ID = process.env.ALL_GP_CHANNEL_ID || "";
const TEST_CHANNEL_ID = process.env.TEST_CHANNEL_ID || "";
const TEST_MODE = String(process.env.TEST_MODE || "true").toLowerCase() === "true";

// Zona horaria para el resumen de las 23:59 (por defecto -6 = Guatemala / CST; pon 0 para UTC)
const TIMEZONE_OFFSET_HOURS = Number(process.env.TIMEZONE_OFFSET_HOURS ?? -6);

if (!DISCORD_TOKEN || !LINK_REDIS_URL || !LINK_REDIS_TOKEN) {
  console.error("❌ Faltan variables obligatorias: DISCORD_TOKEN, LINK_REDIS_URL o LINK_REDIS_TOKEN.");
  process.exit(1);
}

const redis = new Redis({
  url: LINK_REDIS_URL,
  token: LINK_REDIS_TOKEN
});

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers
  ]
});

// ================= HELPERS REDIS Y FECHA =================

function safeJson(val, fallback = null) {
  if (val === null || val === undefined) return fallback;
  if (typeof val === "object") return val;
  try {
    return JSON.parse(val);
  } catch {
    return fallback;
  }
}

async function hostsConocidos() {
  try {
    const raw = await redis.hgetall("zenith:hosts");
    if (!raw || typeof raw !== "object") return [];
    return Object.entries(raw).map(([nombre, val]) => {
      const parsed = safeJson(val, {});
      return { ...parsed, nombre: parsed.nombre || nombre };
    });
  } catch (err) {
    console.error("❌ Error leyendo zenith:hosts:", err.message);
    return [];
  }
}

async function leerGpHits(limite = 250) {
  const rawList = await redis.lrange("zenith:gp_hits", 0, limite - 1);
  if (!Array.isArray(rawList)) return [];
  return rawList
    .map((item) => safeJson(item, null))
    .filter((h) => h && Number(h.ts));
}

function getLocalDateParts(ms = Date.now()) {
  const shifted = new Date(ms + TIMEZONE_OFFSET_HOURS * 3600 * 1000);
  const year = shifted.getUTCFullYear();
  const month = shifted.getUTCMonth() + 1;
  const day = shifted.getUTCDate();
  const hour = shifted.getUTCHours();
  const minute = shifted.getUTCMinutes();
  const isoDate = `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
  return { year, month, day, hour, minute, isoDate };
}

function getDayBoundsMs(isoDate) {
  const [y, m, d] = isoDate.split("-").map(Number);
  const startUtcMs = Date.UTC(y, m - 1, d, 0, 0, 0) - TIMEZONE_OFFSET_HOURS * 3600 * 1000;
  return { startMs: startUtcMs, endMs: startUtcMs + 24 * 3600 * 1000 };
}

// ================= MODO PRUEBA (NO TOCA MARCAS DE REDIS) =================

async function runTestOnce() {
  const targetId = TEST_CHANNEL_ID || ALL_GP_CHANNEL_ID;
  if (!targetId) {
    console.error("❌ Define TEST_CHANNEL_ID en Railway para ejecutar la prueba.");
    return;
  }

  const canal = await client.channels.fetch(targetId).catch(() => null);
  if (!canal) {
    console.error(`❌ No se encontró el canal de prueba ${targetId}.`);
    return;
  }

  const hits = await leerGpHits(1);
  if (!hits.length) {
    console.log("⚠️ zenith:gp_hits está vacío.");
    return;
  }

  const ultimo = hits[0];
  console.log(`🧪 [TEST] Publicando último God Pack (ts=${ultimo.ts}, host=${ultimo.host}) sin tocar marcas...`);

  await canal.send("🧪 **TEST — All God Packs (modo prueba, no toca Redis)**");
  await allgp.publicarGp(canal, ultimo);
  console.log("✅ [TEST] Imagen publicada correctamente. Cambia TEST_MODE=false cuando esté aprobada.");
}

// ================= CICLO DE PRODUCCIÓN (CADA 60 SEGUNDOS) =================

let running = false;
let lastSeenVersion = null;

async function productionTick() {
  if (running) return;
  running = true;

  try {
    // 1. Señal de vida cada minuto para que el bot de respaldo (Monitor Pokemon) no duplique
    await redis.set("zenith:allgp_kyurem", String(Date.now()));

    // 2. Respetar apagado manual si existe zenith:allgp_off = 1
    const offFlag = await redis.get("zenith:allgp_off");
    if (String(offFlag || "") === "1") return;

    const canal = await client.channels.fetch(ALL_GP_CHANNEL_ID).catch(() => null);
    if (!canal) {
      console.error(`❌ No se pudo acceder al canal ALL_GP_CHANNEL_ID (${ALL_GP_CHANNEL_ID}).`);
      return;
    }

    // 3. Revisar si hubo cambios con zenith:gp_hits_v para no bajar la lista innecesariamente
    const currentVersion = await redis.get("zenith:gp_hits_v").catch(() => null);
    const shouldCheckHits = currentVersion === null || String(currentVersion) !== String(lastSeenVersion);

    let cachedHits = null;

    if (shouldCheckHits) {
      let marca = Number(await redis.get("zenith:allgp_ts")) || 0;
      if (!marca) {
        await redis.set("zenith:allgp_ts", String(Date.now()));
        lastSeenVersion = currentVersion;
        console.log("ℹ️ Primera ejecución: zenith:allgp_ts inicializado a ahora.");
      } else {
        cachedHits = await leerGpHits(150);
        const nuevos = cachedHits
          .filter((h) => Number(h.ts) > marca)
          .sort((a, b) => Number(a.ts) - Number(b.ts));

        for (const hit of nuevos) {
          try {
            await allgp.publicarGp(canal, hit);
            await redis.set("zenith:allgp_ts", String(hit.ts));
            console.log(`✅ Publicado GP ts=${hit.ts} (${hit.host || "host"})`);
          } catch (err) {
            console.error(`❌ Error publicando GP ts=${hit.ts}:`, err.message);
            break; // Detener para no saltarnos ninguno si falló temporalmente
          }
        }
        lastSeenVersion = currentVersion;
      }
    }

    // 4. Resumen del día a las 23:59 (ventana 23:59 - 00:10 por si hubo reinicio justo a las 23:59)
    const nowParts = getLocalDateParts();
    const prevParts = getLocalDateParts(Date.now() - 20 * 60 * 1000);
    const targetDay =
      nowParts.hour === 23 && nowParts.minute >= 59
        ? nowParts.isoDate
        : nowParts.hour === 0 && nowParts.minute < 10
        ? prevParts.isoDate
        : null;

    if (targetDay) {
      const lastRecap = String((await redis.get("zenith:allgp_recap")) || "");
      if (lastRecap !== targetDay) {
        const allHits = cachedHits || (await leerGpHits(1000));
        const { startMs, endMs } = getDayBoundsMs(targetDay);
        const hitsDelDia = allHits.filter((h) => Number(h.ts) >= startMs && Number(h.ts) < endMs);

        await redis.set("zenith:allgp_recap", targetDay);
        await allgp.publicarResumen(canal, targetDay, hitsDelDia);
        console.log(`📊 Resumen diario publicado para ${targetDay} (${hitsDelDia.length} GPs).`);
      }
    }
  } catch (err) {
    console.error("🔥 Error en productionTick:", err);
  } finally {
    running = false;
  }
}

// ================= INICIO =================

client.once("ready", async () => {
  console.log(`✅ All-God-Packs conectado como ${client.user.tag} (TEST_MODE=${TEST_MODE})`);

  allgp.iniciar({
    client,
    host: { hostsConocidos },
    motor: () => path.join(__dirname, "motor"),
    log: (...args) => console.log(...args)
  });

  if (TEST_MODE) {
    await runTestOnce();
  } else {
    await productionTick();
    setInterval(productionTick, 60 * 1000);
  }
});

client.login(DISCORD_TOKEN);
