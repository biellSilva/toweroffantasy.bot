from typing import TYPE_CHECKING

from discord import Embed

from src.types import EmojisEnum
from src.utils import convert_rarity_to_color, convert_to_emoji, truncate_value

if TYPE_CHECKING:
    from src.models.weapons import Weapon


class WeaponEmbeds:
    def __init__(self, weapon: "Weapon") -> None:
        self.weapon = weapon
        self._default_embed = Embed(
            title=self.weapon.PREVIEW_NAME,
            url=self.weapon.URL,
            color=convert_rarity_to_color(self.weapon.rarity),
        ).set_thumbnail(url=self.weapon.assets.item_large_icon)

    def main_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()

        embed.description = (
            f"-# **{convert_to_emoji(self.weapon.category.id)} {self.weapon.category.name}**\n"
            f"-# **{convert_to_emoji(self.weapon.element.id)} {self.weapon.element.name}**\n"
            f"{self.weapon.LIMITED_EMOJI}\n"
            f"-# Shatter **{truncate_value(self.weapon.shatter.value)} _{self.weapon.shatter.tier}_**\n"
            f"-# Charge **{truncate_value(self.weapon.charge.value)} _{self.weapon.charge.tier}_**\n\n"
            f"{self.weapon.desc}"
        )

        embed.set_image(url=self.weapon.assets.lottery_drawing)
        embed.set_footer(text="Weapon")

        return [embed]

    def passives_embed(self) -> list[Embed]:
        if not self.weapon.passives:
            embed = self._default_embed.copy().set_footer(text="Passives")
            embed.description = "-# No Passives"
            return [embed]

        embeds: list[Embed] = []

        for passive in self.weapon.passives:
            passive_embed = Embed(
                color=convert_rarity_to_color(self.weapon.rarity),
                description=passive,
            )

            embeds.append(passive_embed)

        embeds[0].title = self.weapon.PREVIEW_NAME
        embeds[0].url = self.weapon.URL
        embeds[0].set_thumbnail(url=self.weapon.assets.item_large_icon)

        embeds[-1].set_footer(text="Passives")

        return embeds

    def multi_element_embed(self, element: str = "Superpower") -> list[Embed]:
        if not self.weapon.multi_element:
            embed = self._default_embed.copy().set_footer(text="Multi-Element")
            embed.description = "-# No multi-element"
            return [embed]

        for multi_element in self.weapon.multi_element:
            if multi_element.element == element:
                embeds: list[Embed] = []

                for passive in multi_element.passives:
                    passive_embed = Embed(
                        color=convert_rarity_to_color(self.weapon.rarity),
                        description=passive,
                    )
                    embeds.append(passive_embed)

                embeds[0].title = self.weapon.PREVIEW_NAME
                embeds[0].url = self.weapon.URL
                embeds[0].set_thumbnail(url=self.weapon.assets.item_large_icon)

                embeds[-1].set_footer(text="Multi-Element")

                return embeds

        embed = self._default_embed.copy().set_footer(text="Multi-Element")
        embed.description = "-# Unknown multi-element"
        return [embed]

    def advancements_embed(self, index: int = 0) -> list[Embed]:
        embed = self._default_embed.copy().set_footer(text="Advancements")
        if not self.weapon.advancements:
            embed.description = "-# No advancements"
            return [embed]

        advance = self.weapon.advancements[index]

        embed.description = (
            f"-# Shatter **{truncate_value(advance.shatter.value)} _{advance.shatter.tier}_**\n"
            f"-# Charge **{truncate_value(advance.charge.value)} _{advance.charge.tier}_**\n\n"
            f"-# **{EmojisEnum.DarkStar.value * (index + 1)}**\n"
            f"{advance.desc}"
        )

        return [embed]

    def skill_embed(self, id_: str | None = None) -> list[Embed]:
        embed = self._default_embed.copy()

        if not self.weapon.skills:
            embed.description = "-# No skills"
            embed.set_footer(text="Skill")
            return [embed]

        if not id_:
            skill_type = self.weapon.skills[0]
            skill = skill_type.attacks[0]
        else:
            skill_type_, skill_id = id_.split("-")

            skill_type = next(
                _skill_type
                for _skill_type in self.weapon.skills
                if _skill_type.type == skill_type_
            )
            skill = next(
                _skill for _skill in skill_type.attacks if _skill.id == skill_id
            )

        if skill.values:
            skill.desc = skill.desc.format(
                *[truncate_value(value[-1]) for value in skill.values]
            )

        if len(skill.desc) < 2000:
            embed.description = (
                f"**{skill.name}**\n"
                f"{f'-# _**{" - ".join(skill.tags)}**_\n' if skill.tags else ''}"
                f"{
                    f'-# **{f" {EmojisEnum.RightArrow} ".join(skill.operations)}**\n\n'
                    if skill.operations
                    else f'-# **{skill_type.name or skill_type.type}**\n\n'
                }"
                f"{skill.desc}"
            )

            embed.set_thumbnail(url=skill.icon).set_footer(text="Skill")

            return [embed]

        embeds: list[Embed] = [embed]

        for ind, desc in enumerate(skill.desc.split("\r\n\r\n")):
            if ind == 0:
                embed.description = (
                    f"**{skill.name}**\n"
                    f"-# _**{' - '.join(skill.tags)}**_\n"
                    f"{
                        f'-# **{f" {EmojisEnum.RightArrow} ".join(skill.operations)}**\n\n'
                        if skill.operations
                        else '\n'
                    }"
                    f"{desc}"
                )
            else:
                embeds.append(
                    Embed(
                        color=convert_rarity_to_color(self.weapon.rarity),
                        description=desc,
                    )
                )

        embeds[-1].set_footer(text="Skill")
        embeds[0].set_thumbnail(url=skill.icon)

        return embeds

    def fashions_embed(self) -> list[Embed]:
        if not self.weapon.fashions:
            embed = self._default_embed.copy()
            embed.description = "-# No fashions available"
            embed.set_footer(text="Fashions")
            return [embed]

        embeds: list[Embed] = []

        for fashion in self.weapon.fashions:
            embed = Embed(
                color=convert_rarity_to_color(self.weapon.rarity),
                description=(
                    f"**{fashion.name}**\n"
                    f"-# _**{fashion.display_type_text}**_\n\n"
                    f"-# {fashion.desc}"
                ),
            )

            embed.set_thumbnail(url=fashion.icon)

            embeds.append(embed)

        embeds[0].title = self.weapon.PREVIEW_NAME
        embeds[0].url = self.weapon.URL
        embeds[-1].set_footer(text="Fashions")

        return embeds
