import discord

from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from src.infra.entitys import Relic


class RelicView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, relic: 'Relic', owner: Union[discord.User, discord.Member]):
        self.relic = relic
        self.owner = owner
        super().__init__(timeout=timeout)

    
    @discord.ui.button(label='Home', style=discord.ButtonStyle.gray)
    async def home_callback(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.relic.embed_main)
    

    @discord.ui.button(label='Advanc', style=discord.ButtonStyle.gray)
    async def advanc_callback(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.relic.embed_advance)