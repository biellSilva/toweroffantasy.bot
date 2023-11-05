
from pydantic import BaseModel


class Shatter(BaseModel):
    'Complementary model for weapon object (shatter)'
    tier: str
    value: str

class Charge(BaseModel):
    'Complementary model for weapon object (charge)'
    tier: str
    value: str

class WeaponPassive(BaseModel):
    'Complementary model for weapon object (passive)'
    title: str
    description: str

class Abilities(BaseModel):
    'Complementary model for weapon object (abilities)'
    name: str
    type: str
    imgSrc: str
    input: list[str] | None = None
    description: str
    breakdown: list[str] | None = None

class RecoMatrices(BaseModel):
    'Complementary model for weapon object (recommended matrices)'
    name: str
    pieces: int
    description: str | None = None
    