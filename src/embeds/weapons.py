from typing import TYPE_CHECKING

from discord import Embed

from src.utils import convert_rarity_to_color, convert_to_emoji

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
        embed = Embed(
            title=self.weapon.PREVIEW_NAME,
            url=self.weapon.URL,
            color=convert_rarity_to_color(self.weapon.rarity),
            description=(
                f"{convert_to_emoji(self.weapon.category.id)} {convert_to_emoji(self.weapon.element.id)} {self.weapon.LIMITED_EMOJI}\n"
                f"*Shatter* {self.weapon.shatter.to_desc}\n"
                f"*Charge* {self.weapon.charge.to_desc}\n"
                f"-# {'\n-# '.join(self.weapon.desc.split('\n'))}\n"
            ),
        )

        embed.set_thumbnail(url=self.weapon.assets.item_large_icon)
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

        return [embed]
