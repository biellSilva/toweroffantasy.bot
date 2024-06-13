from adapters.discord.utils import rarity_to_string
from domain.models.base import EntityBase
from settings import config

from .extras import MountAsset, UnlockItem


class MountSimple(EntityBase):
    name: str
    rarity: int

    @property
    def name_with_rarity(self) -> str:
        return f"[{self.rarity_string}] {self.name}"

    @property
    def rarity_star(self) -> str:
        return config.star_str * self.rarity

    @property
    def rarity_string(self) -> str:
        return rarity_to_string(self.rarity)


class Mount(MountSimple):
    description: str
    assets: MountAsset
    version: str
    unlockItems: list[UnlockItem]
    source: list[str] = []
