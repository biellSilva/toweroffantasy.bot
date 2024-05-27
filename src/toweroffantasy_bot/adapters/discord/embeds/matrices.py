from time import time
from typing import TYPE_CHECKING

from discord import Colour, Embed
from discord.utils import format_dt
from settings import config

if TYPE_CHECKING:
    from domain.models.matrices import Matrix


def info_embed(data: "Matrix") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/matrices/{data.id}",
        colour=Colour.dark_embed(),
        description=data.description,
    )

    embed.set_thumbnail(url=data.assets.iconLarge or data.assets.icon)
    embed.set_footer(text="Info")

    return [embed]


def set_effects_embed(data: "Matrix") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/matrices/{data.id}#effects",
        colour=Colour.dark_embed(),
    )

    embed.description = "\n\n".join(
        [f"**x{effect.need}**\n{effect.description}" for effect in data.sets]
    )

    
    embed.set_thumbnail(url=data.assets.iconLarge or data.assets.icon)
    embed.set_footer(text="Set Effects")

    return [embed]


def banners_embed(data: "Matrix") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/matrices/{data.id}#banners",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assets.iconLarge or data.assets.icon)
    embed.set_footer(text="Banners")

    embed.description = ""

    if not data.banners:
        embed.description = "No banners information available"

        return [embed]

    embed.description += "\n\n".join(
        [
            (
                f"**N° {banner.bannerNumber}**\n"

                f"{format_dt(banner.startDate, "d")} - {(format_dt(banner.endDate, "d") 
                                                         if banner.endDate.timestamp() < time() 
                                                         else format_dt(banner.endDate, "R"))}"
                "\n"

                f"[Details link]({banner.detailsLink})"

                f"{"\n\\- Collab" if banner.isCollab else ""}"
                f"{"\n\\- Limited only" if banner.isLimitedBannerOnly else ""}"
                f"{"\n\\- Final rerun" if banner.isFinalBanner else ""}"
                f"{"\n\\- Release" if not banner.isRerun else ""}"
            )
            for banner in data.banners
        ]
    )

    return [embed]
