
from pydantic import BaseModel


class Skill(BaseModel):
    id: str
    icon: str
    name: str
    description: str

class Skills(BaseModel):
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]

class Stats(BaseModel):
    shatter: int | float
    charge: int | float

class Advancements(BaseModel):
    description: str | None
    stats: Stats
    need: str

class WeaponEffect(BaseModel):
    title: str
    description: str

class ShatterOrCharge(BaseModel):
    value: float
    tier: str

class Assets(BaseModel):
    icon: str | None
    weaponMatrixIcon: str | None
