
from pydantic import BaseModel


class Relic(BaseModel):
    'Base model for relics object'
    name: str
    imgSrc: str
    rarity: str
    description: str
    advancements: list[str]
    videoScr: str = None
    starsInVideo: str = None
    chinaOnly: bool = False

    def __init__(self, **data):
        data['imgSrc'] = f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Artifact/icon/{data["imgSrc"]}.webp'
        super().__init__(**data)