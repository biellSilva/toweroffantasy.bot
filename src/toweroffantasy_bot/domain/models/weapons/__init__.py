from adapters.discord.emojis import BotEmojis
from adapters.discord.utils import rarity_to_string
from domain.models.banner import Banner
from domain.models.base import EntityBase
from domain.models.meta import MetaData

from settings import config

from .extras import (
    BaseStats,
    ShatterOrCharge,
    WeaponAdvancement,
    WeaponAssets,
    WeaponAttacks,
    WeaponEffect,
    WeaponFashion,
    WeaponMats,
)


class WeaponSimple(EntityBase):
    name: str
    rarity: int
    category: str
    element: str

    @property
    def name_with_rarity(self) -> str:
        return f"[{self.rarity_string}] {self.name}"

    @property
    def rarity_star(self) -> str:
        return config.star_str * self.rarity

    @property
    def rarity_string(self) -> str:
        return rarity_to_string(self.rarity)

    @property
    def emoji_element(self) -> str:
        return BotEmojis.get_str(self.element)

    @property
    def emoji_category(self) -> str:
        return BotEmojis.get_str(self.category)


class Weapon(WeaponSimple):
    simulacrumId: str | None
    advanceId: str | None

    assets: WeaponAssets
    limited: bool

    description: str

    shatter: ShatterOrCharge
    charge: ShatterOrCharge

    upgradeMats: WeaponMats | None

    elementEffect: WeaponEffect | None
    weaponEffects: list[WeaponEffect]

    weaponAdvancements: list[WeaponAdvancement]
    weaponAttacks: WeaponAttacks
    weaponStats: list[BaseStats]

    meta: MetaData
    banners: list[Banner]
    fashion: list[WeaponFashion]

    @property
    def stats_emojis(self) -> str:
        return " ".join([BotEmojis.get_str(stat.id) for stat in self.weaponStats])
