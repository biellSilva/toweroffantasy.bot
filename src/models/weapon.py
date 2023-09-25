
from pydantic import BaseModel

from src.config import EMOJIS
from .weapon_extras import *


class Weapon(BaseModel):
    name: str
    imgSrc: str
    element: str
    type: str
    shatter: Shatter
    charge: Charge
    baseStats: list[str]
    materials: list[str]
    weaponEffects: list[WeaponPassive] = None
    advancements: list[str]
    abilities: list[Abilities]
    abilitiesVideoSrc: str = None
    analysisVideoSrc: str = None
    rating: list[float | int] = None
    recommendedPairings: list[str] = None
    recommendedMatrices: list[RecoMatrices]

    def __init__(self, **data):
        data['imgSrc'] = f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/weapon/Icon/{data["imgSrc"]}.webp'
        super().__init__(**data)

    @property
    def element_emoji(self):
        return EMOJIS.get(self.element, self.element)

    @property
    def type_emoji(self):
        return EMOJIS.get(self.type, self.type)
