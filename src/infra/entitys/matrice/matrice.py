
from discord import Embed, Colour
from pydantic import BeforeValidator
from typing import Annotated

from src.utils import convert_rarity

from ..base import EntityBase
from .extra import MatrixAssets, MatrixSet


class MatriceSimple(EntityBase):
    name: str
    rarity: Annotated[str, BeforeValidator(convert_rarity)]


class Matrix(EntityBase):
    name: str
    simulacrumId: str | None
    # type: str
    description: str
    assets: MatrixAssets
    rarity: Annotated[str, BeforeValidator(convert_rarity)]
    sets: list[MatrixSet]



    @property
    def website_url(self):
        return f'https://toweroffantasy.info/matrices/{self.name.replace(" ", "_").lower()}'
    
    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}'

    @property
    def embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.set_thumbnail(url=f'{self.assets.iconLarge}')
        em.set_footer(text='Matrix')

        em.description = f'**{self.description}**\n\n'

        for set in self.sets:
            em.description += f'**{set.need}x**\n{set.description}\n\n'

        
        return em
