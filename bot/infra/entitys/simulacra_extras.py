
from pydantic import BaseModel


class Banner(BaseModel):
    'Complementary model for simulacra object (banner)'
    bannerNo: int
    start: str
    end: str
    subtext: str | None = None

class Banners(BaseModel):
    'Complementary model for simulacra object (list of banner)'
    cn: list[Banner] | None = None
    glob: list[Banner] | None = None

class BestGift(BaseModel):
    'Complementary model for simulacra object (gifts)'
    points: int 
    gift: str 

class Traits(BaseModel):
    'Complementary model for simulacra object (traits)'
    affinity: int 
    description: str

class VoiceActors(BaseModel):
    'Complementary model for simulacra object (voice actors)'
    cn: str | None = None
    jp: str | None = None
    en: str | None = None
    pt: str | None = None
    
