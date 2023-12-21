
from pydantic import BaseModel


class Assets(BaseModel):
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None


class Skill(BaseModel):
    name: str | None
    description: str | None
    icon: str | None
    tags: list[str] 
    operations: list[str]
    id: str | None


class WeaponAttacks(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


class ShatterOrCharge(BaseModel):
    value: float
    tier: str

class WeaponAdvancement(BaseModel):
    description: str | None
    # GoldNeeded: int 
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    # WeaponFashionID: str | None


class FashionWeaponInfo(BaseModel):
    FashionName: str
    FashionImitationId: str


class MatrixSuit(BaseModel):
    MatrixSuitName: str
    MatrixSuitDes: str


class WeaponEffect(BaseModel):
    title: str
    description: str


class RecoMatrix(BaseModel):
    id: str
    pieces: int


class MetaData(BaseModel):
    recommendedPairings: list[str] = []
    recommendedMatrices: list[RecoMatrix] = []
    rating: list[int] = []
    analyticVideoId: str | None = None


class BaseStats(BaseModel):
    id: str
    name: str
    icon:str
    value: float 
    isTag: bool 
    modifier: str


class UpgradeMaterial(BaseModel):
    id: str
    need: int | None


class WeaponMat(BaseModel):
    id: str | None
    amount: int | None
    name: str | None = None
    icon: str | None = None
    type: str | None = None
    description: str | None = None
    rarity: str | None = None


class WeaponMats(BaseModel):
    id: str
    items: list[list[WeaponMat]]