
from pydantic import BeforeValidator
from typing import Annotated
from discord import Embed, Colour

from ..base import EntityBase

from src.utils import convert_rarity
from src.config import STAR_EMOJI


class RelicSimple(EntityBase):
    name: str
    rarity: Annotated[str, BeforeValidator(convert_rarity)] 
    icon: str | None


class Relic(RelicSimple):
    description: str | None
    source: str | None
    advancements: list[str]


    @property
    def embed_base(self):
        em = Embed(colour=Colour.dark_embed())

        em.set_author(name=f'[{self.rarity}] {self.name}', 
                      url='https://toweroffantasy.info/')

        if self.icon:
            em.set_thumbnail(url=self.icon)
    
        return em
    
    @property
    def embed_main(self):
        em = self.embed_base

        em.description = ''

        if self.description:
            em.description += self.description
        
        if self.source:
            if not em.description:
                em.description = self.source
            else:
                em.description += '\n\n' + self.source

        return em
    
    
    @property
    def embed_advance(self):
        em = self.embed_base

        em.description = '\n\n'.join([f'{' '.join([STAR_EMOJI for _ in range(indx)])}\n{advanc}' for indx, advanc in enumerate(self.advancements, start=1)])

        return em