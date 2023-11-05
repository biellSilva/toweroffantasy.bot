import aiohttp

from pydantic import BaseModel
from discord import Embed, Colour

from .simulacra_extras import *
from .weapon import Weapon
from .matrices import Matrice



class Simulacra(BaseModel):
    'Base model for simulacra object'
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
    skinsPreviewUrl: str | None = None
    banners: Banners | None = None
    traits: list[Traits]
    giftTypes: list[str] 
    bestGifts: list[BestGift]
    voiceActors: VoiceActors
    weapon: Weapon
    matrice: Matrice


    @property
    def website_url(self):
        return f'https://toweroffantasy.info/simulacra/{self.name.replace(" ", "-").lower()}'
    
    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}' if self.chinaOnly == False else f'[CN] [{self.rarity}] {self.name}'
    

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

    async def simulacra_embed(self) -> Embed:
        ' Simulacra main embed '
        em = Embed(color=Colour.dark_embed(), 
                           title=self.embed_title,
                           url=self.website_url)
        em.description = ''

        if self.cnName and self.cnName not in ('', ' ', '???'):
            em.description += f"**CN Name:** {self.cnName.capitalize()}\n"
            
        if self.gender and self.gender not in ('', ' ', '???'):
            em.description += f"**Gender:** {self.gender}\n"

        if self.height and self.height not in ('', ' ', '???'):
            em.description += f"**Height:** {self.height}\n"

        if self.birthday and self.birthday not in ('', ' ', '???'):
            em.description += f"**Birthday:** {self.birthday}\n"

        if self.birthplace and self.birthplace not in ('', ' ', '???'):
            em.description += f"**Birthplace:** {self.birthplace}\n"

        if self.horoscope and self.horoscope not in ('', ' ', '???'):
            em.description += f"**Horoscope:** {self.horoscope}\n"

        if self.skinsPreviewUrl:
            em.description += f'\n[Skin Preview]({self.skinsPreviewUrl})'
        
        
        em.set_thumbnail(url=await self.simulacra_image())

        for region, voiceActor in self.voiceActors.model_dump().items():
            if voiceActor == '' or voiceActor == None:
                continue
            
            em.add_field(name=region.upper(), value=voiceActor, inline=True)
        
        return em
    
    async def trait_embed(self) -> Embed:
        ' Trait embed '
        em = Embed(color=Colour.dark_embed(), 
                           title=self.embed_title,
                           url=self.website_url)
        em.set_thumbnail(url=await self.simulacra_image())

        for trait in self.traits:
            em.add_field(name=f'Affinity {trait.affinity}', value=trait.description, inline=False)
    
        return em