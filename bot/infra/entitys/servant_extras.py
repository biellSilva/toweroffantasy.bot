
from pydantic import BaseModel


class ServantAbilitie(BaseModel):
    'Complementary model for Smart-Servant object (servant abilitie)'
    name: str
    effect: str
    imgSrc: int | None = None
    

class ServantGift(BaseModel):
    'Complementary model for Smart-Servant object (servant gift)'
    points: int
    gift: str
    