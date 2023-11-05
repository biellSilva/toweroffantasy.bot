
import discord

from discord.ext import commands
from discord import app_commands

from bot.infra.entitys import Matrice
from bot.core.controller.get_data import get_matrice, get_names


class MatricesCog(commands.Cog):

    '''Matrices Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='matrices')
    @app_commands.describe(name='Matrice name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def matrices(self, interaction: discord.Interaction, name: str):
        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        matrice = await get_matrice(name=name)

        await interaction.edit_original_response(embed=matrice.embed)
    
    @matrices.autocomplete(name='name')
    async def matrices_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=f'[{matrice.rarity}] {matrice.name}' if matrice.chinaOnly == False else f'[CN] [{matrice.rarity}] {matrice.name}',
                value=matrice.name) 
            for matrice in await get_names('matrices') if current.lower() in matrice.name.lower() and isinstance(matrice, Matrice)][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(MatricesCog(bot))
