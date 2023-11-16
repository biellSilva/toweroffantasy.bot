
from discord import Embed, Colour

from bot.config import EMOJIS, STAR_EMOJI
from bot.infra.entitys.base import EntityBase
from .extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Advancements, 
    Skills,
    Assets
)


class Weapon(EntityBase):
    name: str
    description: str
    rarity: str
    type: str 
    element: str
    assets: Assets
    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    advanceID: str | None
    mats: dict[str, int | None]
    weaponEffects: list[WeaponEffect]
    skills: Skills
    advancements: list[Advancements]

    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}'
    
    @property
    def emoji_element(self):
        return EMOJIS.get(self.element, self.element)
    
    @property
    def emoji_type(self):
        return EMOJIS.get(self.type, self.type)
    

    @property
    def embed_main(self) -> Embed:
        em = Embed(colour=Colour.dark_embed(),
                   description=f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                               f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                               f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n'
                               f'*{self.description}*')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        return em
    
    @property
    def embed_effects(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for effect in self.weaponEffects:
            em.description += f'**{effect.title}**\n{effect.description}\n\n'

        return em
    
    @property
    def embed_advanc(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for i, advanc in enumerate(self.advancements, start=1):
            if advanc.description:
                em.description += f'**{i} {STAR_EMOJI}**\n{advanc.description}\n\n'

        return em
    
    @property
    def embed_attacks_normals(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.skills.normals:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em

    @property
    def embed_attacks_dodge(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.skills.dodge:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em
    
    @property
    def embed_attacks_skill(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.skills.skill:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em
    
    @property
    def embed_attacks_discharge(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_type} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.skills.discharge:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em


class WeaponSimple(EntityBase):
    name: str
    rarity: str