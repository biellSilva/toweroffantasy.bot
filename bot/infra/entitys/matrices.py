
from pydantic import BaseModel
from discord import Embed, Colour


class MatriceSet(BaseModel):
    'Complementary model for matrice object (matrice sets)'
    pieces: int
    description: str


class Matrice(BaseModel):
    'Base model for matrice object'
    id: int
    name: str
    rarity: str
    imgSrc: str
    chinaOnly: bool = False
    sets: list[MatriceSet]

    @property
    def image(self):
        return f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/yizhi/256/{self.imgSrc}.webp'
    
    @property
    def website_url(self):
        return f'https://toweroffantasy.info/matrices/{self.name.replace(" ", "-").lower()}'
    
    @property
    def embed(self):
        em = Embed(color=Colour.dark_embed(), 
                   title=f'[{self.rarity}] {self.name}' if self.chinaOnly == False else f'[CN] [{self.rarity}] {self.name}',
                   url = self.website_url)
        
        em.set_thumbnail(url=self.image)

        for set_ in self.sets:
            em.add_field(name=f'{set_.pieces}x Pieces', value=set_.description, inline=False)
        
        return em