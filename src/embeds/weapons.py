from typing import TYPE_CHECKING

from discord import Embed

from src.utils import convert_rarity_to_color, convert_to_emoji

if TYPE_CHECKING:
    from src.models.weapons import Weapon


class WeaponEmbeds:
    def __init__(self, weapon: "Weapon") -> None:
        self.weapon = weapon

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
        embeds: list[Embed] = []

        for passive in self.weapon.passives:
            embed = Embed(
                color=convert_rarity_to_color(self.weapon.rarity),
                description=passive,
            )

            embeds.append(embed)

        if embeds:
            embeds[0].title = self.weapon.PREVIEW_NAME
            embeds[0].url = self.weapon.URL
            embeds[0].set_thumbnail(url=self.weapon.assets.item_large_icon)
            embeds[-1].set_footer(text="Passives")

        return embeds
