from adapters.discord.utils import rarity_to_string
from pydantic import BaseModel
from settings import config


class VoiceActors(BaseModel):
    cn: str | None
    jp: str | None
    en: str | None
    kr: str | None
    pt: str | None


class SimulacraAssets(BaseModel):
    avatar: str | None
    titlePicture: str | None
    characterArtwork: str | None
    painting: str | None
    namePicture: str | None
    grayPainting: str | None
    thumbPainting: str | None
    weaponShowPicture: str | None
    activeImitation: str | None
    inactiveImitation: str | None
    advancePainting: str | None
    advanceGrayPainting: str | None
    backPhoto: str | None
    rarityIcon: str | None
    lotteryCardImage: str | None
    matrixPainting: str | None
    descPainting: str | None


class Awakening(BaseModel):
    name: str | None
    description: str | None
    icon: str | None
    need: int | None


class SimulacraFashionAssets(BaseModel):
    painting: str
    grayPainting: str


class SimulacraFashion(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    source: str
    simulacrumId: str
    weaponId: str
    assets: SimulacraFashionAssets

    @property
    def name_with_rarity(self) -> str:
        return f"[{self.rarity_string}] {self.name}"

    @property
    def rarity_star(self) -> str:
        return config.star_str * self.rarity

    @property
    def rarity_string(self) -> str:
        return rarity_to_string(self.rarity)
