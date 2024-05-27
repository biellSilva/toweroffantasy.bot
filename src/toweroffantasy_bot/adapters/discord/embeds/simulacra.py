from time import time
from typing import TYPE_CHECKING

from discord import Colour, Embed
from discord.utils import format_dt
from settings import config

if TYPE_CHECKING:
    from domain.models.simulacra import Simulacra


def profile_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    embed.set_image(url=data.assetsA0.titlePicture)
    embed.set_footer(text="Profile")

    profile: dict[str, str | None] = data.model_dump(
        include={"affiliation", "homeTown", "birthday", "height", "gender"}
    )

    embed.description = "\n".join(
        [
            f"**{key.capitalize()}:** {value}"
            for key, value in profile.items()
            if value and value.lower() not in ["unknown", "none", "n/a", "/"]
        ]
    )

    # adding second picture if available
    embed_2 = embed.copy()
    embed_2.set_image(
        url=(
            data.assetsA3.titlePicture
            if data.assetsA3
            and data.assetsA0.titlePicture != data.assetsA3.titlePicture
            else None
        )
    )

    return [embed, embed_2]


def awakening_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assetsA0.avatar)

    for awakening in data.awakening:
        if (
            awakening.need
            and awakening.need in (1200, 4000)
            and awakening.name
            and awakening.description
        ):
            embed.add_field(
                name=(
                    awakening.name
                    if ":" not in awakening.name
                    else awakening.name.split(":")[1].strip()
                )
                + f" [{awakening.need}]",
                value=awakening.description,
                inline=False,
            )

    if not embed.fields:
        embed.description = "No awakening information available"

    embed.set_footer(text="Awakening")

    return [embed]


def voice_actors_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assetsA0.avatar)
    embed.set_footer(text="Voice Actors")

    actors: dict[str, str | None] = data.voicing.model_dump()

    embed.description = "\n".join(
        [
            f"**{key.upper()}:** {value}"
            for key, value in actors.items()
            if value and value.lower() not in ["unknown", "none", "n/a", "/"]
        ]
    )

    if not embed.description or embed.description.isspace():
        embed.description = "No voice actors information available"

    return [embed]


def fashion_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    # embed.set_thumbnail(url=data.assetsA0.avatar)
    embed.set_footer(text="Fashion")

    if not data.fashion:
        embed.description = "No fashion information available"

        return [embed]

    embed.description = "\n\n".join(
        [
            (f"**{fashion.name}**\n" f"{fashion.description}\n\n" f"*{fashion.source}*")
            for fashion in data.fashion
        ]
    )

    embeds: list[Embed] = [embed]

    for fashion in data.fashion:
        _fashion_embed = embed.copy()
        _fashion_embed.set_image(url=fashion.assets.painting)
        embeds.append(_fashion_embed)

    return embeds


def liked_gifts_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assetsA0.avatar)
    embed.set_footer(text="Liked Gifts")

    if not data.likedGiftTypes:
        embed.description = "No liked gifts information available"

        return [embed]

    embed.description = "\n".join([f"**{gift}**" for gift in data.likedGiftTypes])

    return [embed]


def banners_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assetsA0.avatar)
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
                f"{"\n\\- Launch" if not banner.isRerun else ""}"
            )
            for banner in data.banners
        ]
    )

    return [embed]


def guidebook_embed(data: "Simulacra") -> list[Embed]:
    if not data.guidebook:
        embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed(),
        description="No guidebook information available"
    )
        return [embed]
    
    
    embeds: list[Embed] = []

    for guidebook in data.guidebook:
        _embed = Embed(colour=Colour.dark_embed())
        _embed.description = f"**{guidebook.title}**\n{guidebook.description}"
        _embed.set_image(url=guidebook.icon)
        embeds.append(_embed)

    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/simulacra/{data.id}"

    embeds[-1].set_footer(text="Guidebook")

    return embeds
