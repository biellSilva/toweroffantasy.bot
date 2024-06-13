from typing import TYPE_CHECKING

from discord import Colour, Embed
from settings import config

if TYPE_CHECKING:
    from domain.models.relics import Relic


def info_embed(data: "Relic") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        description=f"{data.description}\n\n_{data.source}_",
        color=Colour.dark_embed(),
        url=f"{config.tof_info_url}/relics/{data.id}",
    )

    embed.set_thumbnail(url=data.icon)
    embed.set_footer(text="Info")

    return [embed]


def advacements_embed(data: "Relic") -> list[Embed]:

    embeds: list[Embed] = []

    for ind, item in enumerate(data.advancements, start=1):
        embed_ = Embed(
            description=f"**{ind * config.star_str}**\n{item}",
            color=Colour.dark_embed(),
        )
        embeds.append(embed_)

    embeds[-1].set_footer(text="Parts")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/mounts/{data.id}"
    embeds[0].set_thumbnail(url=data.icon)

    return embeds
