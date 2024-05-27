from pydantic import BaseModel


class ShatterOrCharge(BaseModel):
    value: float
    tier: str


class WeaponAssets(BaseModel):
    icon: str | None
    weaponIconForMatrix: str | None
    characterArtwork: str | None


class UpgradeMaterial(BaseModel):
    matId: str | None
    amount: int | None
    name: str | None
    icon: str | None
    type: str | None
    description: str | None
    rarity: int | None


class LevelUpgrade(BaseModel):
    requiredExp: int
    mats: list[UpgradeMaterial]


class WeaponMats(BaseModel):
    id: str
    levels: list[LevelUpgrade]


class WeaponEffect(BaseModel):
    title: str
    description: str


class Skill(BaseModel):
    name: str | None
    description: str | None
    values: list[list[float]]
    icon: str | None
    tags: list[str]
    operations: list[str]
    id: str | None


class WeaponAttacks(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


class AdvancMultipliers(BaseModel):
    statId: str
    coefficient: float


class WeaponAdvancement(BaseModel):
    description: str | None
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    multiplier: list[AdvancMultipliers]


class BaseStats(BaseModel):
    id: str
    name: str
    icon: str | None
    value: float
    upgradeProp: float


class WeaponFashion(BaseModel):
    id: str
    name: str
    icon: str | None
    description: str | None
    rarity: int
    type: str
