import discord

from discord.ext import commands
from discord import app_commands
from unidecode import unidecode

from src.core.service import API
from src.infra.entitys import MatriceSimple, Matrix


class MatriceCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.API = API(simple_model=MatriceSimple,
                       model=Matrix,
                       route='matrice')

    @app_commands.command(name='matrices')
    @app_commands.rename(id='name')
    @app_commands.describe(id='Matrix name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def matrices(self, interaction: discord.Interaction, id: str):
        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        matrice = await self.API.get(id=id, locale=interaction.locale, route='matrices')

        await interaction.edit_original_response(embed=matrice.embed)


    @matrices.autocomplete(name='id')
    async def matrices_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=f'[{matrice.rarity}] {matrice.name}', value=matrice.id) 
            for matrice in await self.API.get_all(locale=interaction.locale, route='matrices') 
            if unidecode(current).lower() in unidecode(matrice.name).lower() 
            or matrice.rarity.lower() == current.lower()
            or unidecode(current).lower() in matrice.id.lower()
        ][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(MatriceCog(bot))
