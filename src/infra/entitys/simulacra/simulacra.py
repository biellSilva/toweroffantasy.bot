
from discord import Embed, Colour
from discord.utils import format_dt
from pydantic import BeforeValidator
from typing import Annotated

from src.config import EMOJIS, STAR_EMOJI
from src.utils import convert_rarity, convert_operations

from ..base import EntityBase
from ..banners import Banner
from .extra import VoiceActors, Awakening, Assets

from ..weapon import Weapon
from ..matrice import Matrix


class SimulacraSimple(EntityBase):
    name: str
    rarity: Annotated[str, BeforeValidator(convert_rarity)]


class Simulacra(EntityBase):
    name: str
    rarity: Annotated[str, BeforeValidator(convert_rarity)]
    avatarId: str
    isReleased: bool
    advanceId: str | None 
    weaponId: str | None
    matrixId: str | None

    assetsA0: Assets
    assetsA3: Assets | None
    
    birthday: str | None
    height: str | None
    gender: str | None
    affiliation: str | None
    homeTown: str | None

    likedGiftTypes: list[str]

    voicing: VoiceActors
    awakening: list[Awakening]
    banners: list[Banner]

    weapon: Weapon | None = None
    matrix: Matrix | None = None

    @property
    def website_url(self):
        return f'https://toweroffantasy.info/simulacra'
    
    @property
    def embed_title(self):
        return f'[{self.rarity}] {self.name}'
    
    @property
    def emoji_element(self):
        if not self.weapon:
            return ''
        return EMOJIS.get(self.weapon.element, self.weapon.element)
    
    @property
    def emoji_category(self):
        if not self.weapon:
            return ''
        return EMOJIS.get(self.weapon.category, self.weapon.category)

    @property
    def emoji_stats(self):
        if not self.weapon:
            return ''
        return ' '.join([EMOJIS.get(stat.id, '') for stat in self.weapon.weaponStats])

    

    @property
    def embed_main(self) -> list[Embed]:
        ' Simulacra main embed '
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = ''

        em.set_thumbnail(url=f'{self.assetsA0.avatar}')
        em.set_image(url=f'{self.assetsA0.titlePicture}')
        em.set_footer(text='Main')

        if self.id == 'imitation_33':
            em.set_image(url=f'{self.assetsA0.painting}')

        em.description += '\n**Voice Actors**\n'

        va: dict[str, str | None] = self.voicing.model_dump()
        for region, voiceActor in va.items():
            if not voiceActor or voiceActor == '':
                continue
            
            em.description += f'**{region.title()}:** *{voiceActor.title()}*\n'
        
        if not self.assetsA3:
            return [em]

        em_a3 = em.copy()
        em_a3.set_image(url=f'{self.assetsA3.titlePicture}')

        return [em, em_a3]

    @property
    def embed_imitation_info(self):
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = ''

        em.set_thumbnail(url=f'{self.assetsA0.avatar}')
        em.set_image(url=f'{self.assetsA0.descPainting}')
        em.set_footer(text='Info')

        if self.gender and self.gender not in ('', ' ', '???'):
            em.description += f"**Gender:** {self.gender}\n"
        
        if self.birthday and self.birthday not in ('', ' ', '???'):
            em.description += f"**Birthday:** {self.birthday}\n"

        if self.height and self.height not in ('', ' ', '???'):
            em.description += f"**Height:** {self.height}\n"

        if self.affiliation and self.affiliation not in ('', ' ', '???'):
            em.description += f"**Affiliation:** {self.affiliation}\n"
        
        if self.homeTown and self.homeTown not in ('', ' ', '???'):
            em.description += f"**Hometown:** {self.homeTown}\n"

        return em
    
    @property
    def embed_trait(self) -> Embed:
        ' Simulacra Traits embed '
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = ''

        em.set_thumbnail(url=f'{self.assetsA0.avatar}')
        em.set_footer(text='Traits')

        for trait in self.awakening:
            em.description += f'**{trait.name}** *[{trait.need} points]*\n{trait.description}\n\n'
        
        return em

    @property
    def embed_banners(self) -> Embed:
        ' Simulacra Banners embed '
        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = ''

        em.set_thumbnail(url=f'{self.assetsA0.avatar}')
        em.set_footer(text='Banners')

        for banner in self.banners:
            em.description += f'**N° {banner.bannerNumber}** | {format_dt(banner.start_datetime, "d")} - {format_dt(banner.end_datetime, "d")}\n'

            if banner.detailsLink:
                em.description += f'[Banner Details]({banner.detailsLink})\n'

            if banner.isLimitedBannerOnly:
                em.description += '\\- Limited banner only\n'
            
            if banner.isCollab:
                em.description += '\\- Collab\n'

            if banner.isRerun:
                em.description += '\\- Rerun\n'

            if banner.isFinalBanner:
                em.description += '\\- Standard after\n'
            
            if banner.noWeapon:
                em.description += '\\- Polymorph\n'

            em.description += '\n'
        
        return em

    @property
    def embed_weapon_main(self) -> Embed:

        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n'
                         f'*{self.weapon.description}*')
        
        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Weapon')

        return em
    
    @property
    def embed_weapon_effects(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Effects')

        if self.weapon.elementEffect:
            em.description += f'**{self.weapon.elementEffect.title}**\n{self.weapon.elementEffect.description}\n\n'

        for effect in self.weapon.weaponEffects:
            em.description += f'**{effect.title}**\n{effect.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')

        return em
    
    @property
    def embed_weapon_advanc(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Advancements')

        for i, advanc in enumerate(self.weapon.weaponAdvancements, start=1):
            if advanc.description:
                em.description += f'**{f"{STAR_EMOJI} " * i}**\n{advanc.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')

        return em
    
    @property
    def embed_weapon_attacks_normals(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Normal Attacks')

        for skill in self.weapon.weaponAttacks.normals:
            if 'Jump' in skill.operations:
                continue

            operations = f'*[{convert_operations(skill.operations)}]*' if skill.operations else ''
            em.description += f'**{skill.name}** {operations}\n{skill.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')
        
        return em
    
    @property
    def embed_weapon_attacks_jump(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Jump Attacks')

        for skill in self.weapon.weaponAttacks.normals:
            if 'Jump' not in skill.operations:
                continue

            operations = f'*[{convert_operations(skill.operations)}]*' if skill.operations else ''
            em.description += f'**{skill.name}** {operations}\n{skill.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')
        
        return em

    @property
    def embed_attacks_dodge(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Dodge Attacks')

        for skill in self.weapon.weaponAttacks.dodge:
            operations = f'*[{convert_operations(skill.operations)}]*' if skill.operations else ''
            em.description += f'**{skill.name}** {operations}\n{skill.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')
        
        return em
    
    @property
    def embed_attacks_skill(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Skill')

        for skill in self.weapon.weaponAttacks.skill:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')
        
        return em
    
    @property
    def embed_attacks_discharge(self) -> Embed:
        
        if not self.weapon:
            raise

        em = Embed(colour=Colour.dark_embed(),
                   title=self.embed_title,
                   url=self.website_url)
        
        em.description = (f'**{self.weapon.name}** {self.emoji_category} {self.emoji_element}\n'
                         f'*Shatter: {self.weapon.shatter.value} **{self.weapon.shatter.tier}***\n'
                         f'*Charge: {self.weapon.charge.value} **{self.weapon.charge.tier}***\n'
                         f'*Stats:* {self.emoji_stats}\n\n')

        em.set_thumbnail(url=f'{self.weapon.assets.icon}')
        em.set_footer(text='Discharge')

        for skill in self.weapon.weaponAttacks.discharge:
            em.description += f'**{skill.name}**\n{skill.description}\n\n'
        
        if em.description.endswith('\n\n'):
            em.description = em.description.removesuffix('\n\n')
        
        return em
    

    @property
    def embed_matrix_main(self) -> Embed:

        if not self.matrix:
            raise

        em = self.matrix.embed
        em.title = self.embed_title
        

        return em