
from pydantic import BaseModel

from .servant_extras import *
from src.config import EMOJIS


class SmartServant(BaseModel):
    name: str
    imgSrc: str
    number: int
    type: str
    element: str
    attack: int
    crit: int
    description: str
    advancements: list[str]
    abilities: list[ServantAbilitie]
    bestGifts: list[ServantGift]

    def __init__(self, **data):
        data['imgSrc'] = f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/PetFight/icon/{data["imgSrc"]}.webp'
        super().__init__(**data)
    
    @property
    def element_emoji(self):
        return EMOJIS.get(self.element, self.element)

    @property
    def type_emoji(self):
        return EMOJIS.get(self.type, self.type)