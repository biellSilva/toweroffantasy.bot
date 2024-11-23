from typing import TYPE_CHECKING

from discord import Interaction, Member, SelectOption, User
from discord.ui import Select

from src.views._base import BaseView

if TYPE_CHECKING:
    from src.embeds.simulacra import SimulacrumEmbeds


class SimulacraView(BaseView):
    def __init__(
        self,
        *,
        controller: "SimulacrumEmbeds",
        timeout: float | None = 180,
        owner: User | Member | None = None,
    ) -> None:
        super().__init__(timeout=timeout, owner=owner)
        self.controller = controller

        self.selector = _SectionSelector(controller)

        self.add_item(self.selector)


class _SectionSelector(Select["SimulacraView"]):
    def __init__(self, controller: "SimulacrumEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self._options = {
            "imitation": controller.imitation_embed,
            "fashions": controller.imitation_fashions_embed,
        }

        self.options = [
            SelectOption(label=option.capitalize(), value=option)
            for option in self._options
        ]

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(embeds=self._options[self.values[0]]())
