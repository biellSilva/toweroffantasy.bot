from typing import Any

from discord import Interaction, Member, User
from discord.ui import View
from discord.ui.item import Item


class BaseView(View):
    def __init__(
        self, *, timeout: float | None = 180, owner: User | Member | None = None
    ) -> None:
        super().__init__(timeout=timeout)
        self.owner = owner

    def validate_owner(self, interaction: Interaction) -> bool:
        return interaction.user == self.owner

    async def interaction_check(self, interaction: Interaction) -> bool:
        return self.validate_owner(interaction)

    async def on_error(
        self, interaction: Interaction, error: Exception, item: Item[Any]
    ) -> None:
        msg = "An error occurred while processing your request. Please try again later."

        if interaction.response.is_done():
            await interaction.followup.send(content=msg, ephemeral=True)
        else:
            await interaction.response.send_message(content=msg, ephemeral=True)

        return await super().on_error(interaction, error, item)
