
from pydantic import BaseModel


class Part(BaseModel):
    'Complementary model for mount object (mount parts)'
    source: str
    imgSrc: str
    guide: str = None
    dropRate: str = None
    video: str = None


class Mount(BaseModel):
    'Base model for mounts object'
    name: str
    imgSrc: str
    id: int
    type: str = ''
    videoScr: str = None
    chinaOnly: bool = False
    parts: list[Part]

    def __init__(self, **data):
        data['imgSrc'] = f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Mount/{data["imgSrc"]}.webp'
        super().__init__(**data)