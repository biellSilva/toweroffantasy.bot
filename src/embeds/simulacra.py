from typing import TYPE_CHECKING

from discord import Embed

from src.utils import convert_rarity_to_color

if TYPE_CHECKING:
    from src.models.imitation import Imitation


class SimulacrumEmbeds:
    def __init__(self, imitation: "Imitation") -> None:
        self.imitation = imitation

    def imitation_embed(self) -> list[Embed]:
        embed = Embed(
            title=self.imitation.PREVIEW_NAME,
            url=self.imitation.URL,
            color=convert_rarity_to_color(self.imitation.rarity),
            description=(
                f"-# {self.imitation.unlock_info} {self.imitation.LIMITED_EMOJI}\n"
                f"{self.imitation.extras.to_description}"
            ),
        )

        embed.set_thumbnail(url=self.imitation.assets.has_got_awaken_entrance)

        embed.set_footer(text="Imitation")

        if not self.imitation.no_weapon:
            embed.set_image(url=self.imitation.assets.title_picture)

        if (
            self.imitation.assets_a3
            and self.imitation.assets_a3.title_picture
            != self.imitation.assets.title_picture
        ):
            embed_clone = embed.copy()
            embed_clone.set_image(url=self.imitation.assets_a3.title_picture)
            return [embed, embed_clone]

        return [embed]

    def imitation_fashions_embed(self) -> list[Embed]:
        embeds: list[Embed] = []

        for fashion in self.imitation.fashions:
            embed = Embed(
                title=fashion.name,
                color=convert_rarity_to_color(self.imitation.rarity),
                description=f"-# {fashion.source}\n-# {fashion.desc}",
            )

            embed.set_thumbnail(url=fashion.assets.painting)

            embeds.append(embed)

        return embeds
