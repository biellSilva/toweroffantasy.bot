from typing import TYPE_CHECKING

from discord import Embed

from src.types import EmojisEnum
from src.utils import convert_rarity_to_color

if TYPE_CHECKING:
    from src.models.imitation import Imitation


class SimulacrumEmbeds:
    def __init__(self, imitation: "Imitation") -> None:
        self.imitation = imitation
        self._default_embed = Embed(
            title=self.imitation.PREVIEW_NAME,
            url=self.imitation.URL,
            color=convert_rarity_to_color(self.imitation.rarity),
        ).set_thumbnail(
            url=self.imitation.assets.big_icon or self.imitation.assets.icon
        )

    def imitation_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()
        embed.description = (
            f"**{self.imitation.unlock_info}** {self.imitation.LIMITED_EMOJI}\n"
            f"{self.imitation.extras.to_description}"
        )

        embed.set_footer(text="Imitation")

        if not self.imitation.no_weapon:
            embed.set_image(url=self.imitation.assets.title_picture)

        embeds = [embed]

        if (
            self.imitation.assets_a3
            and self.imitation.assets_a3.title_picture
            != self.imitation.assets.title_picture
        ):
            embed_clone = embed.copy()
            embed_clone.set_image(url=self.imitation.assets_a3.title_picture)
            embeds.append(embed_clone)

        embeds[-1].set_footer(text="Imitation")

        return embeds

    def fashions_embed(self) -> list[Embed]:
        embeds: list[Embed] = []

        for fashion in self.imitation.fashions:
            embed = Embed(
                title=fashion.name,
                color=convert_rarity_to_color(self.imitation.rarity),
                description=f"-# {fashion.source}\n-# {fashion.desc}",
            )

            embed.set_thumbnail(url=fashion.assets.painting)

            embeds.append(embed)

        if not embeds:
            embed = self._default_embed.copy()
            embed.description = "-# No fashions available"
            embeds.append(embed)

        embeds[-1].set_footer(text="Fashions")

        return embeds

    def buff_likeability_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()
        embed.set_footer(text="Likeabilities")

        for likeability in self.imitation.likeabilities:
            if likeability.type != "buff":
                continue

            embed.add_field(
                name=likeability.name,
                value=(
                    f"-# **\\{EmojisEnum.SparklingHeart} {likeability.condition}**"
                    f"\n{likeability.desc or '-# Unknown'}"
                ),
                inline=False,
            )

        return [embed]

    def voice_actors_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()

        embed.description = "\n".join(
            [
                f"-# {region.capitalize()}\n**{actor}**"
                for region, actor in self.imitation.extras.voice_actors.model_dump().items()
                if actor
            ]
        )

        embed.set_footer(text="Voice Actors")

        return [embed]

    def gifts_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()

        embed.add_field(
            name=f"Likes \\{EmojisEnum.SparklingHeart}",
            value="\n".join([f"-# {gift.name}" for gift in self.imitation.extras.like])
            or "-# No likes",
            inline=False,
        )

        embed.add_field(
            name=f"Dislikes \\{EmojisEnum.BrokenHeart}",
            value="\n".join(
                [f"-# {gift.name}" for gift in self.imitation.extras.dislike]
            )
            or "-# No dislikes",
            inline=False,
        )

        embed.set_footer(text="Gifts")

        return [embed]
