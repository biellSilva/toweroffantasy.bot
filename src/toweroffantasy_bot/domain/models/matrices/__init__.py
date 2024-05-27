from domain.models.banner import Banner
from domain.models.base import EntityBase

from .extra import MatrixAsset, MatrixMeta, MatrixSet


class Matrix(EntityBase):
    name: str
    description: str
    assets: MatrixAsset
    rarity: int
    baseEXP: int
    sets: list[MatrixSet]
    version: str | None
    weaponId: str | None
    simulacrumId: str | None
    banners: list[Banner]
    meta: MatrixMeta
