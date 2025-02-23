from typing import TYPE_CHECKING

from discord import Embed

from src.utils import convert_quality_to_color, convert_to_emoji

if TYPE_CHECKING:
    from src.models.matrices import Suit


class MatrixEmbeds:
    def __init__(self, suit: "Suit") -> None:
        self.suit = suit

        self._default_embed = Embed(
            title=f"[{self.suit.rarity}] {self.suit.name}",
            color=convert_quality_to_color(self.suit.quality),
        ).set_thumbnail(
            url=self.suit.matrices[0].assets.large_icon
            or self.suit.matrices[0].assets.icon
        )

    def sets_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()
        embed.description = f"-# **{self.suit.matrice_name}**"

        embed.set_footer(text="Sets")

        for set_ in self.suit.sets:
            value = set_.description

            if set_.is_global:
                value += "\n-# Background effect"

            embed.add_field(name=f"{set_.needs}x", value=value, inline=False)

        return [embed]

    def pieces_embed(self) -> list[Embed]:
        embed = self._default_embed.copy()

        embed.set_footer(text="Pieces")

        for piece in self.suit.matrices:
            modifiers = " ".join(
                [convert_to_emoji(modifier.id) for modifier in piece.modifiers]
            )
            embed.add_field(
                name=f"{piece.name} [{modifiers}]",
                value=f"-# {piece.description}\n-# **Slot:** {piece.slot_index}",
                inline=False,
            )

        return [embed]
