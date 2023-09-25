import aiohttp

from pydantic import BaseModel

from .simulacra_extras import *
from .weapon import Weapon
from .matrices import Matrice



class Simulacra(BaseModel):
    id: int
    name: str
    cnName: str 
    rarity: str 
    chinaOnly: bool = False
    gender: str 
    height: str 
    birthplace: str 
    birthday: str 
    horoscope: str 
    skinsPreviewUrl: str = None
    banners: Banners = None
    traits: list[Traits]
    giftTypes: list[str] 
    bestGifts: list[BestGift]
    voiceActors: VoiceActors
    weapon: Weapon
    matrice: Matrice


    async def simulacra_image(self):
        async with aiohttp.ClientSession() as cs:
            for image_name in [self.name, self.cnName]:
                if image_name.lower() == 'gnonno':
                    image_name = 'gunonno'

                async with cs.get(f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/huanxing/lihui/{image_name}.webp') as res:
                    if res.status == 200:
                        return res.url
                    
                async with cs.get(f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/huanxing/lihui/{image_name.lower()}.webp') as res:
                    if res.status == 200:
                        return res.url
