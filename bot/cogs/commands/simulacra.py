import discord

from discord.ext import commands
from discord import app_commands

from bot.core.controller.get_data import get_simulacra, get_names
from bot.core.views.simulacra_views import MainView

from bot.infra.entitys import Simulacra



class SimulacraCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='simulacras')
    @app_commands.describe(name='Simulacra name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def simulacra(self, interaction: discord.Interaction, name: str):

        '''
        Simulacra (aka Mimics) are the player's representation of the characters found in Tower of Fantasy.
        '''

        await interaction.response.defer()

        simulacra = await get_simulacra(name=name)

        await interaction.edit_original_response(embed=await simulacra.simulacra_embed(), 
                                                 view=MainView(simulacra=simulacra, owner=interaction.user))

    @simulacra.autocomplete(name='name')
    async def simulacra_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=f'[{simulacra.rarity}] {simulacra.name}' if simulacra.chinaOnly == False else f'[CN] [{simulacra.rarity}] {simulacra.name}',
                value=simulacra.name) 
            for simulacra in await get_names('simulacras') 
            if current.lower() in simulacra.name.lower() and isinstance(simulacra, Simulacra)][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(SimulacraCog(bot))
