
from pydantic import BaseModel



class MatriceSet(BaseModel):
    pieces: int
    description: str


class Matrice(BaseModel):
    id: int
    name: str
    rarity: str
    imgSrc: str
    chinaOnly: bool = False
    sets: list[MatriceSet]

    def __init__(self, **data):
        data['imgSrc'] = f'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/yizhi/256/{data["imgSrc"]}.webp'
        super().__init__(**data)