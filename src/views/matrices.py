from typing import TYPE_CHECKING

from discord import Interaction, Member, SelectOption, User
from discord.ui import Select

from src.views._base import BaseView

if TYPE_CHECKING:
    from src.embeds.matrices import MatrixEmbeds


class MatrixView(BaseView):
    def __init__(
        self,
        *,
        controller: "MatrixEmbeds",
        timeout: float | None = 180,
        owner: User | Member | None = None,
    ) -> None:
        super().__init__(timeout=timeout, owner=owner)
        self.controller = controller

        self.selector = _SectionSelector(controller)

        self.add_item(self.selector)


class _SectionSelector(Select["MatrixView"]):
    def __init__(self, controller: "MatrixEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self._options = {
            "sets": controller.sets_embed,
            "pieces": controller.pieces_embed,
        }

        self.options = [
            SelectOption(label=option.title(), value=option) for option in self._options
        ]

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(embeds=self._options[self.values[0]]())
