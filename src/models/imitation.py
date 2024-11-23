from pydantic import BaseModel

from src._settings import config
from src.models.base import BackgroundColor
from src.types import EmojisEnum


class _FashionAssets(BaseModel):
    painting: str
    gray_painting: str


class _ImitationFashion(BaseModel):
    id: str
    name: str
    desc: str
    source: str
    imitation_id: str
    quality: str
    only_weapon: bool
    assets: _FashionAssets


class _SimulacrumGift(BaseModel):
    id: str
    name: str
    background_color: BackgroundColor


class _SimulacrumVoiceActors(BaseModel):
    chinese: str | None
    japanese: str | None
    english: str | None
    korean: str | None
    portuguese: str | None


class _ImitationExtras(BaseModel):
    gender: str | None
    birthday: str | None
    age: str
    height: str | None
    title: str
    job: str
    belong_to: str | None
    hometown: str | None
    hometown_map: str | None
    experience_record: str | None
    character: str | None

    like: list[_SimulacrumGift]
    dislike: list[_SimulacrumGift]

    voice_actors: _SimulacrumVoiceActors

    @property
    def to_description(self) -> str:
        _data = self.model_dump(
            exclude={
                "like",
                "dislike",
                "voice_actors",
                "hometown_map",
                "character",
                "experience_record",
            },
            exclude_none=True,
        )

        return "\n".join(
            [
                f"-# **{key.replace("_", " ").capitalize()}:** {value}"
                for key, value in _data.items()
            ]
        )


class _ImitationAssets(BaseModel):
    name_picture: str | None
    name_2_picture: str | None
    name_3_picture: str | None
    desc_painting: str | None
    painting: str | None
    gray_painting: str | None
    thumb_painting: str | None
    weapon_show_picture: str | None
    has_got_awaken_entrance: str | None
    not_got_awaken_entrance: str | None
    card_adv_page: str | None
    advance_painting: str | None
    advance_gray_painting: str | None
    back_photo: str | None
    rarity_icon: str | None
    job_back: str | None
    motto_picture: str | None
    motto_2_picture: str | None
    title_picture: str | None
    imitation_virtual_shadow: str | None
    awaken_name_picture: str | None
    awaken_photo: str | None


class Imitation(BaseModel):
    id: str
    name: str
    desc: str
    unlock_info: str
    sex: str
    rarity: str
    weapon_id: str | None
    avatar_id: str
    is_limited: bool
    no_weapon: bool

    fashions: list[_ImitationFashion]
    extras: _ImitationExtras

    assets: _ImitationAssets
    assets_a3: _ImitationAssets

    @property
    def URL(self) -> str:
        return f"{config.WEBSITE_URL}/simulacra/{self.id}"

    @property
    def PREVIEW_NAME(self) -> str:
        return f"[{self.rarity}] {self.name}"

    @property
    def LIMITED_EMOJI(self) -> str:
        if self.no_weapon:
            return ""
        return (
            str(EmojisEnum.BallRed) if self.is_limited else str(EmojisEnum.BallsMixed)
        )
