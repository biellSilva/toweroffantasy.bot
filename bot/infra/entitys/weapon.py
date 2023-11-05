
from pydantic import BaseModel
from discord import Embed, Colour

from bot.config import EMOJIS
from .weapon_extras import *


class Weapon(BaseModel):
    name: str
    imgSrc: str
    element: str
    type: str
    shatter: Shatter
    charge: Charge
    baseStats: list[str]
    materials: list[str]
    weaponEffects: list[WeaponPassive] | None = None
    advancements: list[str]
    abilities: list[Abilities]
    abilitiesVideoSrc: str | None = None
    analysisVideoSrc: str | None = None
    rating: list[float | int] | None = None
    recommendedPairings: list[str] | None = None
    recommendedMatrices: list[RecoMatrices]

    @property
    def element_emoji(self):
        return EMOJIS.get(self.element, self.element)

    @property
    def type_emoji(self):
        return EMOJIS.get(self.type, self.type)
    
    @property
    def base_stats(self):
        return ' '.join(EMOJIS.get(stats.lower(), stats.title()) for stats in self.baseStats)

    @property
    def image(self):
        return f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/weapon/Icon/{self.imgSrc}.webp'
    
    @property
    def main_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        if self.analysisVideoSrc:
            em.description += f'\n[Analysis Video]({self.analysisVideoSrc})'
        
        if self.abilitiesVideoSrc:
            em.description += f'\n[Abilities Video]({self.abilitiesVideoSrc})'

        if self.weaponEffects:
            for effect in self.weaponEffects:
                em.add_field(name=effect.title, value=effect.description, inline=False)

        return em


    @property
    def advanc_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        for ind, advanc in enumerate(self.advancements, start=1):
            em.add_field(name=f'{ind} ★', value=advanc, inline=False)

        return em
    

    @property
    def meta_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        if self.recommendedPairings and len(self.recommendedPairings) != 0:
            em.add_field(name='Recommended Pairings', 
                            value='\n'.join(f'**[{name.capitalize()}](https://toweroffantasy.info/simulacra/{name.replace(" ","-").lower()})**' 
                                            for name in self.recommendedPairings), 
                            inline=False)

        if self.recommendedMatrices and len(self.recommendedMatrices) != 0:
            em.add_field(name='Recommended Matrices', 
                            value='\n'.join(f'**[{matrix.pieces}x {matrix.name.capitalize()}](https://toweroffantasy.info/matrices/{matrix.name.replace(" ","-").lower()})**' 
                                            for matrix in self.recommendedMatrices), 
                            inline=False)

        return em
    
    @property
    def normal_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        for abilitie in self.abilities:
            if 'normal' in abilitie.type:
                if abilitie.input and 'Jump' not in abilitie.input:
                    input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input)} ]*"

                    em.description += f"\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n"
                    
                    if abilitie.breakdown:
                        em.description += '**Breakdown:**\n'
                        em.description += '\n'.join(abilitie.breakdown)

                elif not abilitie.input:
                    em.description += f"\n**{abilitie.name}** \n{abilitie.description}\n"
                        
                    if abilitie.breakdown:
                        em.description += '**Breakdown:**\n'
                        em.description += '\n'.join(abilitie.breakdown)

                em.description += '\n'
        return em
    
    @property
    def jump_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        for abilitie in self.abilities:
            if 'normal' in abilitie.type and abilitie.input and 'Jump' in abilitie.input:
                input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input).title()} ]*"

                em.description += f"\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n"
                
                if abilitie.breakdown:
                    em.description+= '**Breakdown:**\n'
                    em.description+= '\n'.join(abilitie.breakdown)
                
                em.description += '\n'

        return em
    
    @property
    def dodge_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        
        for abilitie in self.abilities:
            if 'dodge' in abilitie.type:

                input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input).title()} ]*"

                em.description += f"\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n"
                
                if abilitie.breakdown:
                    em.description+= '**Breakdown:**\n'
                    em.description+= '\n'.join(abilitie.breakdown)

                em.description += '\n'
        return em
    
    @property
    def skill_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        for abilitie in self.abilities:
            if 'skill' in abilitie.type:
                em.description += f"\n\n**{abilitie.name.title()}** *[ {abilitie.type.capitalize()} ]*\n{abilitie.description}"

        return em
    
    @property
    def discharge_embed(self) -> Embed:
        em = Embed(colour=Colour.dark_embed())
        em.description = (f"**{self.name}** {self.element_emoji} {self.type_emoji}\n"
                          f"Shatter: *{self.shatter.value} **{self.shatter.tier}***\n"
                          f"Charge: *{self.charge.value} **{self.charge.tier}***\n"
                          f"Base stats: *{self.base_stats}*\n")
        
        em.set_thumbnail(url=self.image)
        
        for abilitie in self.abilities:
            if 'discharge' in abilitie.type:
                em.description += f"\n\n**{abilitie.name.title()}** *[ {abilitie.type.capitalize()} ]*\n{abilitie.description}"

        return em