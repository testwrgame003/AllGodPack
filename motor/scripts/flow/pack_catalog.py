"""Pack catalog - Updated for v1.8.1 with Series C1 & Special Pack: First Partners (SP1)

Each entry carries:
  - `hg_cost`: LARGE hourglasses PurchaseV2 spends per pack open (0 = free pack).
  - `power_id`: Pack power pool used ("PACK_POWER_NORMAL" or "PACK_POWER_SPECIAL").
  - `default_packs`: Recommended packs per account (2 for normal, 1 for SP1).
"""

DEFAULT_PAID_PACK_ID = "CN001_0010_00_000"  # Dual Fusion: Mega Mewtwo X (C1)
DEFAULT_PRODUCT_ID = "PC_PS_2610000_01_01_01"
DEFAULT_HG_COST = 12


PAID_HOURGLASS_PACKS = [
    # ─── C1 & SP1 (Featured / Current) ───
    {
        "name": "Dual Fusion: Mega Mewtwo X",
        "expansion_id": "c1",
        "sku_id": "C1_1",
        "pack_id": "CN001_0010_00_000",
        "product_id": "PC_PS_2610000_01_01_01",
        "hg_cost": 12,
        "power_id": "PACK_POWER_NORMAL",
        "default_packs": 2,
    },
    {
        "name": "Dual Fusion: Pikachu",
        "expansion_id": "c1",
        "sku_id": "C1_2",
        "pack_id": "CN001_0020_00_000",
        "product_id": "PC_PS_2610000_01_02_01",
        "hg_cost": 12,
        "power_id": "PACK_POWER_NORMAL",
        "default_packs": 2,
    },
{
        "name": "First Partners / Primeros Compañeros (Free)",
        "expansion_id": "sp1",
        "sku_id": "SP1_1",
        "pack_id": "SP001_0010_00_000",
        "product_id": "PC_PS_2610010_01_01_01",
        "hg_cost": 0,
        "power_id": "PACK_POWER_SPECIAL",
        "default_packs": 1,
    },
    # ─── B Series ───
    {"name": "Deluxe Mega", "expansion_id": "b4b", "sku_id": "B4b_1", "pack_id": "BN011_0010_00_000", "product_id": "PC_PS_2609000_01_01_01", "hg_cost": 0},
    {"name": "Team Rocket's Ambition", "expansion_id": "b4a", "sku_id": "B4a_1", "pack_id": "BN010_0010_00_000", "product_id": "PC_PS_2608000_01_01_01", "hg_cost": 0},
    {"name": "Ruler of the Skies", "expansion_id": "b4", "sku_id": "B4_1", "pack_id": "BN009_0010_00_000", "product_id": "PC_PS_2607000_01_01_01"},
    {"name": "Everyday Wonders", "expansion_id": "b3b", "sku_id": "B3b_1", "pack_id": "BN008_0010_00_000", "product_id": "PC_PS_2606000_01_01_01"},
    {"name": "Paradox Drive", "expansion_id": "b3a", "sku_id": "B3a_1", "pack_id": "BN007_0010_00_000", "product_id": "PC_PS_2605000_01_01_01"},
    {"name": "Pulsing Aura", "expansion_id": "b3", "sku_id": "B3_1", "pack_id": "BN006_0010_00_000", "product_id": "PC_PS_2604000_01_01_01"},
    {"name": "Mega Shine", "expansion_id": "b2b", "sku_id": "B2b_1", "pack_id": "BN005_0010_00_000", "product_id": "PC_PS_2603000_01_01_01"},
    {"name": "Paldean Wonders", "expansion_id": "b2a", "sku_id": "B2a_1", "pack_id": "BN004_0010_00_000", "product_id": "PC_PS_2602000_01_01_01"},
    {"name": "Fantastical Parade", "expansion_id": "b2", "sku_id": "B2_1", "pack_id": "BN003_0010_00_000", "product_id": "PC_PS_2601000_01_01_01"},
    {"name": "Crimson Blaze", "expansion_id": "b1a", "sku_id": "B1a_1", "pack_id": "BN002_0010_00_000", "product_id": "PC_PS_2600000_01_01_01"},
    {"name": "Mega Rising: Mega Blaziken", "expansion_id": "b1", "sku_id": "B1_1", "pack_id": "BN001_0010_00_000", "product_id": "PC_PS_2510000_01_01_01"},
    {"name": "Mega Rising: Mega Gyarados", "expansion_id": "b1", "sku_id": "B1_2", "pack_id": "BN001_0020_00_000", "product_id": "PC_PS_2510000_01_02_01"},
    {"name": "Mega Rising: Mega Altaria", "expansion_id": "b1", "sku_id": "B1_3", "pack_id": "BN001_0030_00_000", "product_id": "PC_PS_2510000_01_03_01"},
    # ─── A Series ───
    {"name": "Wisdom of Sea and Sky: Ho-Oh", "expansion_id": "a4", "sku_id": "A4_1", "pack_id": "AN009_0010_00_000", "product_id": "PC_PS_2509000_01_01_01"},
    {"name": "Wisdom of Sea and Sky: Lugia", "expansion_id": "a4", "sku_id": "A4_2", "pack_id": "AN009_0020_00_000", "product_id": "PC_PS_2509000_01_02_01", "hg_cost": 12},
    {"name": "Eevee Grove", "expansion_id": "a3b", "sku_id": "A3b_1", "pack_id": "AN008_0010_00_000", "product_id": "PC_PS_2506000_01_01_01"},
    {"name": "Extradimensional Crisis", "expansion_id": "a3a", "sku_id": "A3a_1", "pack_id": "AN007_0010_00_000", "product_id": "PC_PS_2507000_01_01_01"},
    {"name": "Celestial Guardians: Solgaleo", "expansion_id": "a3", "sku_id": "A3_1", "pack_id": "AN006_0010_00_000", "product_id": "PC_PS_2506000_01_01_01"},
    {"name": "Celestial Guardians: Lunala", "expansion_id": "a3", "sku_id": "A3_2", "pack_id": "AN006_0020_00_000", "product_id": "PC_PS_2506000_01_01_01"},
    {"name": "Shining Revelry", "expansion_id": "a2b", "sku_id": "A2b_1", "pack_id": "AN005_0010_00_000", "product_id": "PC_PS_2503010_01_01_01"},
    {"name": "Triumphant Light", "expansion_id": "a2a", "sku_id": "A2a_1", "pack_id": "AN004_0010_00_000", "product_id": "PC_PS_2504000_01_01_01"},
    {"name": "Space-Time Smackdown: Dialga", "expansion_id": "a2", "sku_id": "A2_1", "pack_id": "AN003_0010_00_000", "product_id": "PC_PS_2503000_01_01_01"},
    {"name": "Space-Time Smackdown: Palkia", "expansion_id": "a2", "sku_id": "A2_2", "pack_id": "AN003_0020_00_000", "product_id": "PC_PS_2409010_01_02_01"},
    {"name": "Mythical Island", "expansion_id": "a1a", "sku_id": "A1a_1", "pack_id": "AN002_0010_00_000", "product_id": "PC_PS_2502000_01_01_01"},
    {"name": "Genetic Apex: Mewtwo", "expansion_id": "a1", "sku_id": "A1_1", "pack_id": "AN001_0010_00_000", "product_id": "PC_PS_2501000_01_01_01"},
    {"name": "Genetic Apex: Charizard", "expansion_id": "a1", "sku_id": "A1_2", "pack_id": "AN001_0020_00_000", "product_id": "PC_PS_2501000_01_01_01"},
    {"name": "Genetic Apex: Pikachu", "expansion_id": "a1", "sku_id": "A1_3", "pack_id": "AN001_0030_00_000", "product_id": "PC_PS_2501000_01_01_01"},
]

for _p in PAID_HOURGLASS_PACKS:
    _p.setdefault("hg_cost", DEFAULT_HG_COST)
    _p.setdefault("power_id", "PACK_POWER_NORMAL")
    _p.setdefault("default_packs", 2)
del _p

PAID_HOURGLASS_PACK_IDS = {pack["pack_id"] for pack in PAID_HOURGLASS_PACKS}
PAID_HOURGLASS_PACKS_BY_ID = {pack["pack_id"]: pack for pack in PAID_HOURGLASS_PACKS}


def paid_pack_options() -> list[dict]:
    """Return copy-safe pack option dictionaries for UIs."""
    return [dict(pack) for pack in PAID_HOURGLASS_PACKS]


def normalize_paid_pack_id(pack_id: str | None) -> str:
    pack_id = (pack_id or "").strip()
    return pack_id if pack_id in PAID_HOURGLASS_PACK_IDS else DEFAULT_PAID_PACK_ID


def product_id_for_pack(pack_id: str | None) -> str:
    norm_id = normalize_paid_pack_id(pack_id)
    pack = PAID_HOURGLASS_PACKS_BY_ID.get(norm_id, {})
    if "product_id" in pack:
        return str(pack["product_id"] or "")
    return DEFAULT_PRODUCT_ID


def hg_cost_for_pack(pack_id: str | None) -> int:
    normalized = normalize_paid_pack_id(pack_id)
    if normalized not in PAID_HOURGLASS_PACKS_BY_ID:
        return 0
    return int(PAID_HOURGLASS_PACKS_BY_ID[normalized].get(
        "hg_cost", DEFAULT_HG_COST) or 0)


def power_id_for_pack(pack_id: str | None) -> str:
    pack = PAID_HOURGLASS_PACKS_BY_ID.get(normalize_paid_pack_id(pack_id), {})
    return str(pack.get("power_id") or "PACK_POWER_NORMAL")


def is_special_single_pack(pack_id: str | None) -> bool:
    pid = (pack_id or "").strip().upper()
    if pid.startswith("SP") or pid.startswith("CN002"):
        return True
    pack = PAID_HOURGLASS_PACKS_BY_ID.get(pid, {})
    return pack.get("expansion_id") == "sp1" or pack.get("default_packs") == 1
