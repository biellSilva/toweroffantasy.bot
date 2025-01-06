from __future__ import annotations

from pydantic import BaseModel

from src._settings import config
from src.types import EmojisEnum


class Element(BaseModel):
    id: str
    name: str
    desc: str
    icon: str

    @property
    def to_desc(self) -> str:
        return f"{self.name} {self.icon}"


class Category(BaseModel):
    id: str
    name: str
    icon: str
    icon_gray: str

    @property
    def to_desc(self) -> str:
        return f"{self.name} {self.icon}"


class ShatterOrCharge(BaseModel):
    value: float
    tier: str

    @property
    def to_desc(self) -> str:
        return f"*{self.tier}* **{self.value}**"


class Attack(BaseModel):
    id: str
    name: str
    desc: str
    short_desc: str | None
    icon: str
    tags: list[str]
    operations: list[str]
    values: list[list[float]]


class Skill(BaseModel):
    name: str | None
    desc: str | None
    type: str
    icon: str
    attacks: list[Attack]


class Attribute(BaseModel):
    id: str
    value: float


class NeedItem(BaseModel):
    id: str
    count: int


class Advancement(BaseModel):
    desc: str
    attributes: list[Attribute]
    need_item: NeedItem
    cost_type: str
    need_golds: int
    star_skill_score: int
    shatter: ShatterOrCharge
    charge: ShatterOrCharge


class Fashion(BaseModel):
    id: str
    name: str
    desc: str
    use_desc: str
    brief: str
    icon: str
    quality: str
    display_type_text: str


class RecommendedMatrice(BaseModel):
    id: str
    reason: str


class Assets(BaseModel):
    item_icon: str
    item_large_icon: str
    weapon_icon_for_matrix: str
    solo_league_ban_pick_banner: str
    item_name_image: str
    lottery_drawing: str
    lottery_card_image: str


class MultiElement(BaseModel):
    element: str
    passives: list[str]


class WeaponSimple(BaseModel):
    id: str
    name: str
    desc: str
    brief: str
    lottery_desc: str
    rarity: str
    quality: str

    is_fate: bool
    is_limited: bool
    is_warehouse: bool

    element: Element
    category: Category

    shatter: ShatterOrCharge
    charge: ShatterOrCharge
    assets: Assets

    @property
    def URL(self) -> str:
        return f"{config.WEBSITE_URL}/weapons/{self.id}"

    @property
    def PREVIEW_NAME(self) -> str:
        return f"[{self.rarity}] {self.name}"

    @property
    def LIMITED_EMOJI(self) -> str:
        return (
            str(EmojisEnum.BallRed) if self.is_limited else str(EmojisEnum.BallsMixed)
        )


class Weapon(WeaponSimple):
    skills: list[Skill] = []
    advancements: list[Advancement] = []
    passives: list[str] = []
    multi_element: list[MultiElement] = []
    fashions: list[Fashion] = []
    recommended_matrices: list[RecommendedMatrice] = []
