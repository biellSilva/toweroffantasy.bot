
from discord import Colour, Embed

from ....config import EMOJIS, STAR_EMOJI
from ..base import EntityBase
from .extra import (
    ShatterOrCharge, 
    WeaponEffect, 
    Assets,
    MetaData,
    BaseStats,
    # FashionWeaponInfo,
    # MatrixSuit,
    WeaponAdvancement,
    WeaponAttacks,
    WeaponMats
)


class Weapon(EntityBase):
    simulacrumId: str | None
    advanceId: str | None
    # isUpPoolWeapon: bool = False

    name: str
    rarity: str
    assets: Assets

    # Brief: str
    category: str
    element: str
    description: str

    shatter: ShatterOrCharge
    charge: ShatterOrCharge

    # FashionWeaponInfos: list[FashionWeaponInfo]
    # RecommendedMatrices: list[MatrixSuit]

    # upgradeMats: WeaponMats | None

    elementEffect: WeaponEffect | None
    weaponEffects: list[WeaponEffect]

    weaponAdvancements: list[WeaponAdvancement]
    weaponAttacks: WeaponAttacks 
    weaponStats: list[BaseStats]

    meta: MetaData


    
    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}'
    
    @property
    def emoji_element(self):
        return EMOJIS.get(self.element, self.element)
    
    @property
    def emoji_category(self):
        return EMOJIS.get(self.category, self.category)
    

    @property
    def embed_main(self) -> Embed:
        em = Embed(colour=Colour.dark_embed(),
                   description=f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                               f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                               f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n'
                               f'*{self.description}*')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        return em
    
    @property
    def embed_effects(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for effect in self.weaponEffects:
            em.description += f'**{effect.title}**\n{effect.description}\n\n'

        return em
    
    @property
    def embed_advanc(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for i, advanc in enumerate(self.weaponAdvancements, start=1):
            if advanc.description:
                em.description += STAR_EMOJI * i + f'\n{advanc.description}\n\n'

        return em
    
    @property
    def embed_attacks_normals(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.weaponAttacks.normals:
            if 'Jump' not in skill.operations:
                em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em
    
    @property
    def embed_attacks_jumps(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.weaponAttacks.normals:
            if 'Jump' in skill.operations:
                em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em

    @property
    def embed_attacks_dodge(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.weaponAttacks.dodge:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em
    
    @property
    def embed_attacks_skill(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.weaponAttacks.skill:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em
    
    @property
    def embed_attacks_discharge(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())

        em.description = (f'**{self.embed_title}** {self.emoji_category} {self.emoji_element}\n'
                          f'*Shatter: {self.shatter.value} **{self.shatter.tier}***\n'
                          f'*Charge: {self.charge.value} **{self.charge.tier}***\n\n')

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.icon}')

        for skill in self.weaponAttacks.discharge:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        return em


class WeaponSimple(EntityBase):
    name: str
    rarity: str