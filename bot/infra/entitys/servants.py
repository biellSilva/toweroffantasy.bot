
from pydantic import BaseModel
from discord import Embed, Colour

from .servant_extras import *
from bot.config import EMOJIS


class SmartServant(BaseModel):
    'Base model for Smart-Servant object'
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

    
    @property
    def element_emoji(self):
        return EMOJIS.get(self.element, self.element)

    @property
    def type_emoji(self):
        return EMOJIS.get(self.type, self.type)
    
    @property
    def attack_emoji(self):
        return EMOJIS.get('attack', '')

    @property
    def crit_emoji(self):
        return EMOJIS.get('crit', '')
    
    @property
    def image(self):
        return f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/PetFight/icon/{self.imgSrc}.webp'


    @property
    def embed_advanc(self) -> Embed:
        em = Embed(color=Colour.dark_embed(), 
                   title=self.name,
                   description=f'{self.type_emoji} {self.element_emoji}\n'
                               f'Attack: **{self.attack}** {self.attack_emoji}\n'
                               f'Crit: **{self.crit}** {self.crit_emoji}\n\n'
                               f'{self.description}')
        em.set_thumbnail(url=self.image)

        for star, advanc in enumerate(self.advancements, start=1):
            em.add_field(name=f'{star} ★', value=f'{advanc}', inline=False)

        return em

    @property
    def embed_abilitys(self) -> Embed:
        em = Embed(color=Colour.dark_embed(), 
                   title=self.name,
                   description=f'{self.type_emoji} {self.element_emoji}\n'
                               f'Attack: **{self.attack}** {self.attack_emoji}\n'
                               f'Crit: **{self.crit}** {self.crit_emoji}\n\n'
                               f'{self.description}')
        em.set_thumbnail(url=self.image)

        for abilit in self.abilities:
            em.add_field(name=abilit.name, value=abilit.effect, inline=False)

        return em