
from discord import Embed, Colour

from ..base import EntityBase

from .extra import MatriceSet


class Matrice(EntityBase):
    name: str
    type: str
    description: str
    icon: str
    rarity: str
    set: MatriceSet

    @property
    def website_url(self):
        return f'https://toweroffantasy.info/matrice/{self.name.replace(" ", "_").lower()}'
    
    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}'

    @property
    def embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.icon}')
        em.description = f'> **{self.description}**'

        if self.set.set_2:
            em.description += '\n'

            if self.rarity == 'N':
                em.description += f'\n**4x**'
            elif self.rarity == 'R':
                em.description += f'\n**3x**'
            elif self.rarity == 'SR':
                em.description += f'\n**3x**'
            elif self.rarity == 'SSR':
                em.description += f'\n**2x**'

            em.description += f'\n{self.set.set_2}'
        
        if self.set.set_4:
            em.description += '\n'

            if self.rarity == 'SSR':
                em.description += f'\n**4x**'

            em.description += f'\n{self.set.set_4}'
        
        return em




class MatriceSimple(EntityBase):
    name: str
    rarity: str