import discord

from typing import Union

from bot.infra.entitys import Relic


class RelicView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, relic: Relic, owner: Union[discord.User, discord.Member]):
        self.relic = relic
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='relic_home', label='Home', style=discord.ButtonStyle.grey)
    async def relic_home_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.relic.embed)

    @discord.ui.button(custom_id='relic_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def relic_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.relic.embed_stars)
            