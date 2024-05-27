from adapters.discord.emojis import BotEmojis
from adapters.discord.utils import rarity_to_string
from domain.models.banner import Banner
from domain.models.base import EntityBase
from domain.models.meta import MetaData

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


class Weapon(EntityBase):
    simulacrumId: str | None
    advanceId: str | None

    name: str
    version: str | None
    rarity: int
    assets: WeaponAssets
    limited: bool

    category: str
    element: str

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
    def name_with_rarity(self) -> str:
        return f"[{self.rarity_string}] {self.name}"

    @property
    def rarity_star(self) -> str:
        return "★" * self.rarity

    @property
    def rarity_string(self) -> str:
        return rarity_to_string(self.rarity)

    @property
    def emoji_element(self) -> str:
        return BotEmojis.get_str(self.element)

    @property
    def emoji_category(self) -> str:
        return BotEmojis.get_str(self.category)
