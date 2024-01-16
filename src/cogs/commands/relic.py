import discord

from discord.ext import commands
from discord import app_commands
from unidecode import unidecode

from src.core.service import API
from src.infra.entitys import RelicSimple, Relic
from src.core.views.relic import RelicView


class RelicsCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.API = API(simple_model=RelicSimple,
                       model=Relic,
                       route='relics')

    @app_commands.command(name='relics')
    @app_commands.rename(id='name')
    @app_commands.describe(id='Relic name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def relics(self, interaction: discord.Interaction, id: str):
        '''
        Matrices (aka Chips) are items that can be attached to weapon slots.
        '''

        await interaction.response.defer()

        relic = await self.API.get(id=id, locale=interaction.locale, route='relics')

        await interaction.edit_original_response(embed=relic.embed_main, view=RelicView(relic=relic, owner=interaction.user))


    @relics.autocomplete(name='id')
    async def relics_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=f'[{relic.rarity}] {relic.name}', value=relic.id) 
            for relic in await self.API.get_all(locale=interaction.locale, route='relics') 
            if unidecode(current).lower() in unidecode(relic.name).lower() 
            or relic.rarity.lower() == current.lower()
            or unidecode(current).lower() in relic.id.lower()
        ][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(RelicsCog(bot))
