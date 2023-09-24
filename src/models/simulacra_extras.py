
from pydantic import BaseModel


class Banner(BaseModel):
    bannerNo: int
    start: str
    end: str
    subtext: str = None

class Banners(BaseModel):
    cn: list[Banner] = None
    glob: list[Banner] = None

class BestGift(BaseModel):
    points: int 
    gift: str 

class Traits(BaseModel):
    affinity: int 
    description: str

class VoiceActors(BaseModel):
    cn: str = None
    jp: str = None
    en: str = None
    pt: str = None
    
