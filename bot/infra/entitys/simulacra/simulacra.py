
from discord import Embed, Colour
from discord.utils import format_dt

from ..base import EntityBase
from .extra import VoiceActors, Awakening, Assets, Banner

from ..weapon import Weapon
from ..matrice import Matrice


class Simulacra(EntityBase):
    name: str
    avatarID: str
    advanceID: str | None 
    assets: Assets
    weaponID: str | None
    age: str
    height: str
    gender: str
    state: str
    city: str
    rating: str
    gift_types: list[str]
    voice_actors: VoiceActors
    awakenings: list[Awakening]
    banners: list[Banner]

    @property
    def website_url(self):
        return f'https://toweroffantasy.info/simulacra/{self.name.replace(" ", "_").lower()}'
    
    @property
    def embed_title(self):
        return self.name

    @property
    def embed_main(self) -> Embed:
        ' Simulacra main embed '
        em = Embed(colour=Colour.dark_embed(),
                      title=f'{self.embed_title} - Home',
                      url=self.website_url)
        em.description = ''

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.avatar}')
        em.set_image(url=f'https://api.toweroffantasy.info{self.assets.lotteryDrawing}')

            
        if self.gender and self.gender not in ('', ' ', '???'):
            em.description += f"**Gender:** {self.gender}\n"
        
        if self.age and self.age not in ('', ' ', '???'):
            em.description += f"**Birthday:** {self.age}\n"

        if self.height and self.height not in ('', ' ', '???'):
            em.description += f"**Height:** {self.height}\n"

        if self.state and self.state not in ('', ' ', '???'):
            em.description += f"**State:** {self.state}\n"
        
        if self.city and self.city not in ('', ' ', '???'):
            em.description += f"**City:** {self.city}\n"

        return em
    
    @property
    def embed_VA(self) -> Embed:
        ' Simulacra Voice Actors embed '
        em = Embed(colour=Colour.dark_embed(),
                      title=f'{self.embed_title} - Voice Actors',
                      url=self.website_url)
        em.description = ''

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.avatar}')

        for region, voiceActor in self.voice_actors.model_dump().items():
            if voiceActor == '' or voiceActor == None:
                continue
            
            em.description += f'**{region.title()}:** *{voiceActor.title()}*\n'
        
        return em
    
    @property
    def embed_trait(self) -> Embed:
        ' Simulacra Traits embed '
        em = Embed(colour=Colour.dark_embed(),
                      title=f'{self.embed_title} - Traits',
                      url=self.website_url)
        em.description = ''

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.avatar}')

        for trait in self.awakenings:
            em.description += f'**{trait.name}**\n{trait.description}\n\n'
        
        return em

    @property
    def embed_banners(self) -> Embed:
        ' Simulacra Banners embed '
        em = Embed(colour=Colour.dark_embed(),
                      title=f'{self.embed_title} - Banners',
                      url=self.website_url)
        em.description = ''

        em.set_thumbnail(url=f'https://api.toweroffantasy.info{self.assets.avatar}')

        for banner in self.banners:
            em.description += f'**N° {banner.bannerNo}** | {format_dt(banner.start_datetime, "d")} - {format_dt(banner.end_datetime, "d")}\n'

            if banner.details_link:
                em.description += f'[Banner Details]({banner.details_link})\n'

            if banner.limited_banner_only:
                em.description += '\\- Limited banner only\n'
            
            if banner.is_collab:
                em.description += '\\- Collab\n'

            if banner.is_rerun:
                em.description += '\\- Rerun\n'

            if banner.final_rerun:
                em.description += '\\- Standard after\n'
            
            em.description += '\n'
        
        return em


class SimulacraV2(Simulacra):
    weapon: Weapon | None
    matrice: Matrice | None


class SimulacraSimple(EntityBase):
    name: str
    assets: Assets
    weaponID: str | None