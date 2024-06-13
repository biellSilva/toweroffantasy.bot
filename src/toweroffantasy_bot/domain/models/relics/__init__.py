from adapters.discord.utils import rarity_to_string
from domain.models.base import EntityBase
from settings import config


class RelicSimple(EntityBase):
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


class Relic(RelicSimple):
    description: str | None
    source: str | None
    type: str
    icon: str | None
    version: str | None
    advancements: list[str]
