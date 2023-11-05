
from pydantic import BaseModel
from discord import Embed, Colour

class Relic(BaseModel):
    'Base model for relics object'
    name: str
    imgSrc: str
    rarity: str
    description: str
    advancements: list[str]
    videoScr: str | None = None
    starsInVideo: str | None = None
    chinaOnly: bool = False

    @property
    def image(self):
        return f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Artifact/icon/{self.imgSrc}.webp'
    
    @property
    def website_url(self):
        if 'overdrive' in self.name.lower():
            return f'https://toweroffantasy.info/relics/booster-shot'
        else:
            return f'https://toweroffantasy.info/relics/{self.name.replace(" ", "-").lower()}'
    
    @property
    def embed(self) -> Embed:
        em = Embed(color=Colour.dark_embed(), 
                           title=f'[{self.rarity}] {self.name}' if self.chinaOnly == False else f'[CN] [{self.rarity}] {self.name}',
                           url=self.website_url,
                           description=self.description)
        
        em.set_thumbnail(url=self.image)

        return em
    
    @property
    def embed_stars(self) -> Embed:
        em = Embed(color=Colour.dark_embed(), 
                           title=f'[{self.rarity}] {self.name}' if self.chinaOnly == False else f'[CN] [{self.rarity}] {self.name}',
                           url=self.website_url)
        
        em.set_thumbnail(url=self.image)
        em.description=''
        
        for star, advanc in enumerate(self.advancements, start=1):
            em.description += f'**{star} ★**\n{advanc}\n\n'

        return em