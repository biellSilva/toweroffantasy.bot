
import re

from discord import Embed, Colour
from pydantic import BaseModel


class Part(BaseModel):
    'Complementary model for mount object (mount parts)'
    source: str
    imgSrc: str
    guide: str | None = None
    dropRate: str | None = None
    video: str | None = None


class Mount(BaseModel):
    'Base model for mounts object'
    name: str
    imgSrc: str
    id: int
    type: str | None = None
    videoScr: str | None = None
    chinaOnly: bool = False
    parts: list[Part]
    
    @property
    def image(self):
        return f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Mount/{self.imgSrc}.webp'

    @property
    def website_url(self):
        return f'https://toweroffantasy.info/mounts/{self.name.replace(" ", "-").lower()}'

    @property
    def embed(self) -> Embed:
        em = Embed(title = f'{self.name}' if self.chinaOnly == False else f'[CN] {self.name}',
                   color = Colour.dark_embed(),
                   url = self.website_url)
        
        em.description = ''
        
        if self.type:
            em.description += f'**Type:** {self.type}\n\n'

        for i, part in enumerate(self.parts, start=1):
            result = re.sub(r"\(/([A-Za-z]+(/[A-Za-z]+)+)\.[A-Za-z0-9]+\)", '', part.source, 0, re.MULTILINE)
            result = result.replace('[', '').replace(']', '').replace('<abbr title=\'China Exclusive\'></abbr>', '**[CN]**').replace('\n\n', '\n')

            em.description += f'**Part {i}** \n{result}\n'

            if part.dropRate: 
                em.description += f'**Drop rate:** {part.dropRate}\n'

            if part.guide:
                em.description += f'[Guide]({part.guide})\n'

            if part.video:
                em.description += f'[Video Part]({part.video})\n'

            em.description += '\n'

        if self.videoScr:
            em.description += f'\n[Video Preview]({self.videoScr})'
        
        em.set_thumbnail(url=self.image)
        
        return em