
from pydantic import BaseModel



class Shatter(BaseModel):
    tier: str
    value: str

class Charge(BaseModel):
    tier: str
    value: str

class WeaponPassive(BaseModel):
    title: str
    description: str

class Abilities(BaseModel):
    name: str
    type: str
    imgSrc: str
    input: list[str] = None
    description: str
    breakdown: list[str] = None

class RecoMatrices(BaseModel):
    name: str
    pieces: int
    description: str = None
    