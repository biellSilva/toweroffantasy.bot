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
        url=f"{config.tof_info_url}/simulacra/{data.id}#profile",
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
        url=f"{config.tof_info_url}/simulacra/{data.id}#awakening",
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
        url=f"{config.tof_info_url}/simulacra/{data.id}#voice-actors",
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

    if not data.fashion:
        embed.description = "No fashion information available"
        embed.set_footer(text="Fashion")
        return [embed]

    embed.description = f"**{data.fashion[0].name}**\n*{data.fashion[0].source}*\n{data.fashion[0].description}"
    embed.set_image(url=data.fashion[0].assets.painting)

    embeds: list[Embed] = [embed]

    for fashion in data.fashion[1:]:
        _embed = Embed(colour=Colour.dark_embed())

        _embed.description = f"**{fashion.name}**\n*{fashion.source}*\n{fashion.description}"
        _embed.set_image(url=fashion.assets.painting)

        embeds.append(_embed)

    embeds[-1].set_footer(text="Fashion")

    return embeds


def liked_gifts_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}#preferred-gifts",
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
        url=f"{config.tof_info_url}/simulacra/{data.id}#banners",
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
                f"{"\n\\- Release" if not banner.isRerun else ""}"
            )
            for banner in data.banners
        ]
    )

    return [embed]


def guidebook_embed(data: "Simulacra") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/simulacra/{data.id}",
        colour=Colour.dark_embed())
    
    embed.set_footer(text="Guidebook")

    if not data.guidebook:
        embed.description="No guidebook information available"
        return [embed]
    
    embed.description = f"**{data.guidebook[0].title}**\n{data.guidebook[0].description}"
    embed.set_image(url=data.guidebook[0].icon)

    return [embed]
