from adapters.discord.utils import rarity_to_string
from domain.models.banner import Banner
from domain.models.base import EntityBase
from domain.models.guidebook.extra import GuideBookItem
from domain.models.matrices import Matrix
from domain.models.weapons import Weapon
from settings import config

from .extra import Awakening, SimulacraAssets, SimulacraFashion, VoiceActors


class SimulacraSimple(EntityBase):
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


class Simulacra(SimulacraSimple):
    version: str | None
    isReleased: bool
    limited: bool
    avatarId: str
    advanceId: str | None
    unlockInfo: str
    weaponId: str
    matrixId: str
    likedGiftTypes: list[str]
    dislikedGiftTypes: list[str]
    gender: str | None
    birthday: str | None
    height: str | None
    affiliation: str | None
    homeTown: str | None
    assetsA0: SimulacraAssets
    assetsA3: SimulacraAssets | None
    voicing: VoiceActors
    awakening: list[Awakening]
    banners: list[Banner]
    fashion: list[SimulacraFashion]
    guidebook: list[GuideBookItem]

    weapon: Weapon | None
    matrix: Matrix | None
