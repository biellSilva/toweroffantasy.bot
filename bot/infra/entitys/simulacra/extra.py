
from pydantic import BaseModel, Field


class VoiceActors(BaseModel):
    chinese: str | None = Field(alias='cn')
    japanese: str | None = Field(alias='jp')
    english: str | None = Field(alias='en')
    korean: str | None = Field(alias='kr')
    portuguese: str | None = Field(alias='pt')


class Awakening(BaseModel):
    name: str
    description: str
    icon: str
    need: int


class Assets(BaseModel):
    avatar: str
    titlePicture: str
    painting: str
    namePicture: str
    grayPainting: str
    thumbPainting: str
    weaponShowPicture: str
    activeImitation: str
    inactiveImitation:str
    advancePainting: str
    advanceGrayPainting: str
    backPhoto: str
    rarityIcon: str
    lotteryCardImage: str
    # lotteryDrawing: str
    matrixPainting: str
    descPainting: str
