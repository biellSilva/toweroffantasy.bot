from adapters.discord.utils import rarity_to_string
from domain.models.banner import Banner
from domain.models.base import EntityBase
from settings import config

from .extra import MatrixAsset, MatrixMeta, MatrixSet


class MatrixSimple(EntityBase):
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


class Matrix(MatrixSimple):
    description: str
    assets: MatrixAsset
    baseEXP: int
    sets: list[MatrixSet]
    version: str | None
    weaponId: str | None
    simulacrumId: str | None
    banners: list[Banner]
    meta: MatrixMeta
