import discord

from discord.ext import commands
from discord import app_commands
from unidecode import unidecode

from src.core.views.simulacra import SimulacraView
from src.core.service.api import API

from src.infra.entitys import Simulacra, SimulacraSimple


class SimulacraCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.API = API(
            simple_model=SimulacraSimple,
            model=Simulacra,
            route='simulacra'
        )


    @app_commands.command(name='simulacrum')
    @app_commands.rename(id='name')
    @app_commands.describe(id='Simulacrum name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def simulacra(self, interaction: discord.Interaction, id: str):
        '''
        Simulacra (aka Mimics) are the player's representation of the characters found in Tower of Fantasy.
        '''

        await interaction.response.defer()

        simulacra = await self.API.get(id=id, locale=interaction.locale, route='simulacra-v2')

        await interaction.edit_original_response(embeds=simulacra.embed_main, 
                                                 view=SimulacraView(simulacra=simulacra, 
                                                                    owner=interaction.user))

    @simulacra.autocomplete(name='id')
    async def simulacra_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=f'[{simulacra.rarity}] {simulacra.name}', value=simulacra.id) 
            for simulacra in await self.API.get_all(locale=interaction.locale, route='simulacra') 
            if unidecode(current).lower() in unidecode(simulacra.name).lower()
            or simulacra.rarity.lower() == current.lower()
            or unidecode(current).lower() in simulacra.id.lower()
        ][:25]
    
    
async def setup(bot: commands.Bot):
    await bot.add_cog(SimulacraCog(bot))
