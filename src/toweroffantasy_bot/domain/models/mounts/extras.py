from adapters.discord.utils import rarity_to_string
from pydantic import BaseModel
from settings import config


class MountAsset(BaseModel):
    icon: str | None
    showImage: str | None


class MountPart(BaseModel):
    id: str
    name: str
    description: str
    rarity: int
    icon: str
    type: str

    @property
    def name_with_rarity(self) -> str:
        return f"[{self.rarity_string}] {self.name}"

    @property
    def rarity_star(self) -> str:
        return config.star_str * self.rarity

    @property
    def rarity_string(self) -> str:
        return rarity_to_string(self.rarity)


class UnlockItem(BaseModel):
    amount: int
    item: MountPart
