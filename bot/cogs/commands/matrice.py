import discord

from discord.ext import commands
from discord import app_commands

from bot.core.service.api import TofAPI

from bot.infra.entitys import Matrice, MatriceSimple


class MatriceCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.API = TofAPI(
            simple_model=MatriceSimple,
            model=Matrice,
            route='matrice'
        )


    @app_commands.command(name='matrice')
    @app_commands.rename(id='name')
    @app_commands.describe(id='Matrice name')
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

        matrice = await self.API.get(id=id, locale=interaction.locale)

        await interaction.edit_original_response(embed=matrice.embed)


    @matrices.autocomplete(name='id')
    async def matrices_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=f'[{matrice.rarity}] {matrice.name}', value=matrice.id) 
            for matrice in await self.API.get_all(locale=interaction.locale) 
            if current.lower() in matrice.name.lower()
        ][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(MatriceCog(bot))
