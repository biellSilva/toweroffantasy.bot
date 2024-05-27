from time import time
from typing import TYPE_CHECKING

from discord import Colour, Embed
from discord.utils import format_dt
from settings import config

if TYPE_CHECKING:
    from domain.models.weapons import Weapon
    from domain.models.weapons.extras import Skill

def stats_embed(data: "Weapon") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/weapons/{data.id}#stats",
        colour=Colour.dark_embed(),
        description=(
            f"{data.emoji_element} {data.emoji_category}\n"
            f"{data.stats_emojis}\n"
            f"Shatter: **{data.shatter.tier}** {data.shatter.value}\n"
            f"Charge: **{data.charge.tier}** {data.charge.value}\n\n"
            f"*{data.description}*"
        ),
    )

    embed.set_thumbnail(url=data.assets.icon)
    embed.set_footer(text="Stats")

    return [embed]


def weapon_effects_embed(data: "Weapon") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/weapons/{data.id}#effects",
        colour=Colour.dark_embed(),
    )
    if not data.elementEffect:
        embed.description = "No element effect"

    else:
        embed.description = (
            f"**{data.elementEffect.title}**\n{data.elementEffect.description}"
        )

    embeds: list[Embed] = [embed]

    for effect in data.weaponEffects:
        embeds.append(
            Embed(
                colour=Colour.dark_embed(),
                description=f"**{effect.title}**\n{effect.description}",
            )
        )

    embeds[-1].set_footer(text="Weapon Effects")

    return embeds


def fashion_embed(data: "Weapon") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/weapons/{data.id}",
        colour=Colour.dark_embed(),
    )

    if not data.fashion:
        embed.description = "No fashion information available"
        embed.set_footer(text="Fashion")
        return [embed]

    embed.description = f"**{data.fashion[0].name}**\n{data.fashion[0].description}"
    embed.set_image(url=data.fashion[0].icon)

    embeds: list[Embed] = [embed]

    for fashion in data.fashion[1:]:
        _embed = Embed(colour=Colour.dark_embed())

        _embed.description = f"**{fashion.name}**\n{fashion.description}"
        _embed.set_image(url=fashion.icon)

        embeds.append(_embed)

    embeds[-1].set_footer(text="Fashion")

    return embeds


def advancements_embed(data: "Weapon") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/weapons/{data.id}#advancements",
        colour=Colour.dark_embed(),
    )

    if not data.weaponAdvancements:
        embed.description = "No advancements information available"
        embed.set_footer(text="Advancements")
        return [embed]

    embeds: list[Embed] = [embed]

    for ind, advancement in enumerate(data.weaponAdvancements, start=1):
        if ind == 1:
            embeds[0].description = (
                f"**{config.star_str * ind}**\n{advancement.description}"
            )
            continue

        _embed = Embed(
            colour=Colour.dark_embed(),
            description=f"**{config.star_str * ind}**\n{advancement.description}",
        )

        embeds.append(_embed)

    embeds[-1].set_footer(text="Advancements")

    return embeds

def banners_embed(data: "Weapon") -> list[Embed]:
    embed = Embed(
        title=data.name_with_rarity,
        url=f"{config.tof_info_url}/weapons/{data.id}#banners",
        colour=Colour.dark_embed(),
    )

    embed.set_thumbnail(url=data.assets.icon)
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

def __attack_format_desc(description: str | None, values: list[list[float]]) -> str:
    def truncate_values(values: list[float]) -> list[float | int]:
        return [value if value % 1 != 0 else int(value) for value in values]

    if values:
        return description.format(*truncate_values(values[-1])) if description else ""
    return description or "N/A"

def __weapon_attack(attack: "Skill") -> Embed:
    _embed = Embed(
        colour=Colour.dark_embed(), 
        description = (
            f"**{attack.name}** \u200b\u200b *Max Level*\n"

            f"{
                f"*{" - ".join(attack.tags)}*\n" 
                if attack.tags else ''
              }"

            f"{
                f"*{" - ".join(attack.operations)}*\n" 
                if attack.operations else ''
              }"

            f"{__attack_format_desc(attack.description, attack.values)}"
            ))

    _embed.set_thumbnail(url=attack.icon)

    return _embed

def normal_attacks_embed(data: "Weapon") -> list[Embed]:

    if not data.weaponAttacks.normals:
        embed = Embed(
            title=data.name_with_rarity,
            url=f"{config.tof_info_url}/weapons/{data.id}#skills",
            colour=Colour.dark_embed(),
        )
        embed.set_thumbnail(url=data.assets.icon)
        embed.set_footer(text="Normal Attacks")
        embed.description = "No normal attacks information available"
        return [embed]

    embeds: list[Embed] = []

    for attack in data.weaponAttacks.normals:
        embeds.append(__weapon_attack(attack))

    embeds[-1].set_footer(text="Normal Attacks")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/weapons/{data.id}#skills"

    return embeds

def dodge_attacks_embed(data: "Weapon") -> list[Embed]:

    if not data.weaponAttacks.dodge:
        embed = Embed(
            title=data.name_with_rarity,
            url=f"{config.tof_info_url}/weapons/{data.id}#skills",
            colour=Colour.dark_embed(),
        )
        embed.set_thumbnail(url=data.assets.icon)
        embed.set_footer(text="Dodge attacks")
        embed.description = "No dodge attacks information available"
        return [embed]

    embeds: list[Embed] = []

    for attack in data.weaponAttacks.dodge:
        embeds.append(__weapon_attack(attack))

    embeds[-1].set_footer(text="Dodge Attacks")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/weapons/{data.id}#skills"

    return embeds


def skills_attacks_embed(data: "Weapon") -> list[Embed]:

    if not data.weaponAttacks.skill:
        embed = Embed(
            title=data.name_with_rarity,
            url=f"{config.tof_info_url}/weapons/{data.id}#skills",
            colour=Colour.dark_embed(),
        )
        embed.set_thumbnail(url=data.assets.icon)
        embed.set_footer(text="Skill attacks")
        embed.description = "No skill attacks information available"
        return [embed]

    embeds: list[Embed] = []

    for attack in data.weaponAttacks.skill:
        embeds.append(__weapon_attack(attack))

    embeds[-1].set_footer(text="Skill Attacks")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/weapons/{data.id}#skills"

    return embeds

def discharge_attacks_embed(data: "Weapon") -> list[Embed]:

    if not data.weaponAttacks.discharge:
        embed = Embed(
            title=data.name_with_rarity,
            url=f"{config.tof_info_url}/weapons/{data.id}#skills",
            colour=Colour.dark_embed(),
        )
        embed.set_thumbnail(url=data.assets.icon)
        embed.set_footer(text="Discharge attacks")
        embed.description = "No discharge attacks information available"
        return [embed]

    embeds: list[Embed] = []

    for attack in data.weaponAttacks.discharge:
        embeds.append(__weapon_attack(attack))

    embeds[-1].set_footer(text="Discharge Attacks")
    embeds[0].title = data.name_with_rarity
    embeds[0].url = f"{config.tof_info_url}/weapons/{data.id}#skills"

    return embeds
