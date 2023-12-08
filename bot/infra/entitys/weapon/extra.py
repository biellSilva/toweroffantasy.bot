
from pydantic import BaseModel


class Skill(BaseModel):
    name: str | None
    description: str | None
    # Values: list[list[ListKeys]] = []
    icon: str | None
    tags: list[str] 
    operations: list[str] 

class Skills(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]

class Stats(BaseModel):
    shatter: int | float
    charge: int | float

class ShatterOrCharge(BaseModel):
    value: float
    tier: str

class Advancements(BaseModel):
    description: str | None = None
    # GoldNeeded: int 
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    need: str | None
    # WeaponFashionID: str | None

class WeaponEffect(BaseModel):
    title: str
    description: str

class Assets(BaseModel):
    icon: str | None
    # itemLargeIcon: str | None
    # WeaponUPIcon: str | None
    weaponIconForMatrix: str | None

class RecoMatrix(BaseModel):
    id: str
    pieces: int

class MetaData(BaseModel):
    recommendedPairings: list[str]
    recommendedMatrices: list[RecoMatrix]
    rating: list[int]
    analyticVideoId: str | None

class BaseStats(BaseModel):
    id: str
    name: str
    icon: str