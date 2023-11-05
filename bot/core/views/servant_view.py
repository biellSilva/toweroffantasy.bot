import discord
from typing import Union

from bot.infra.entitys import SmartServant


class ServantView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, servant: SmartServant, owner: Union[discord.User, discord.Member]):
        self.servant = servant
        self.owner = owner
        super().__init__(timeout=timeout)


    @discord.ui.button(custom_id='servant_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def servant_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.servant.embed_advanc)


    @discord.ui.button(custom_id='servant_abilit', label='Abilities', style=discord.ButtonStyle.grey)
    async def servant_abilit_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.servant.embed_abilitys)
    