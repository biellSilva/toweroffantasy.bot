
from pydantic import BaseModel


class ServantAbilitie(BaseModel):
    name: str
    effect: str
    imgSrc: int = None
    

class ServantGift(BaseModel):
    points: int
    gift: str
    