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
            title=f"{self.weapon.PREVIEW_NAME} {self.weapon.LIMITED_EMOJI}",
            url=self.weapon.URL,
            color=convert_rarity_to_color(self.weapon.rarity),
            description=(
                f"-# {self.weapon.desc}\n"
                f"-# {convert_to_emoji(self.weapon.category.id)} {convert_to_emoji(self.weapon.element.id)}\n"
                f"-# {self.weapon.shatter.to_desc} | {self.weapon.charge.to_desc}"
            ),
        )

        embed.set_thumbnail(url=self.weapon.assets.item_large_icon)

        embed.set_footer(text="Weapon")

        return [embed]
