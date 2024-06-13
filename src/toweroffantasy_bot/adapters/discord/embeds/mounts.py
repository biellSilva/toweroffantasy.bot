from typing import TYPE_CHECKING

from discord import Colour, Embed
from settings import config

if TYPE_CHECKING:
    from domain.models.mounts import Mount


def info_embed(data: "Mount") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        description=data.description,
        color=Colour.dark_embed(),
        url=f"{config.tof_info_url}/mounts/{data.id}",
    )

    embed.set_image(url=data.assets.icon)
    embed.set_footer(text="Info")

    return [embed]


def unlock_items_embed(data: "Mount") -> list[Embed]:

    embeds: list[Embed] = []

    for item in data.unlockItems:
        embed_ = Embed(
            description=f"**{item.amount}x {item.item.name}**\n*{item.item.description}*",
            color=Colour.dark_embed(),
        )

        embed_.set_thumbnail(url=item.item.icon)
        embeds.append(embed_)

    embeds[-1].set_footer(text="Parts")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/mounts/{data.id}"

    return embeds
