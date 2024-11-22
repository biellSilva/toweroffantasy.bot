from typing import TYPE_CHECKING

from discord import Embed

from src.utils import convert_quality_to_color, convert_to_emoji, split_matrix_name

if TYPE_CHECKING:
    from src.models.matrices import MatrixSuit


class MatrixEmbeds:
    def __init__(self, suit: "MatrixSuit") -> None:
        self.suit = suit

    def sets_embed(self) -> Embed:
        matrix = self.suit.matrices[0]

        embed = Embed(
            title=f"[{matrix.rarity}] {split_matrix_name(matrix.name)}",
            color=convert_quality_to_color(self.suit.quality),
            description=f"-# {self.suit.name}",
        )
        embed.set_footer(text="Sets")

        for set_ in self.suit.sets:
            value = set_.description

            if set_.is_global:
                value += "\n-# Background effect"

            embed.add_field(name=f"{set_.needs}x", value=value, inline=False)

        return embed

    def pieces_embed(self) -> Embed:
        embed = Embed(color=convert_quality_to_color(self.suit.quality))
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

        return embed
