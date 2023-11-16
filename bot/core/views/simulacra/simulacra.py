
import discord

from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from bot.infra.entitys import Simulacra


class SimulacraView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label='Main', style=discord.ButtonStyle.grey)
    async def main_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_main)


    @discord.ui.button(label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_trait)

    
    @discord.ui.button(label='Voice Actors', style=discord.ButtonStyle.grey)
    async def voice_actors_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_VA)

    
    @discord.ui.button(label='Banners', style=discord.ButtonStyle.grey)
    async def banners_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_banners)

