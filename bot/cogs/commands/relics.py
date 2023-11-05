import discord

from discord.ext import commands
from discord import app_commands

from bot.core.views.relic_view import RelicView
from bot.core.controller.get_data import get_relic, get_names
from bot.infra.entitys import Relic


class RelicsCog(commands.Cog):

    '''Relics Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='relics')
    @app_commands.describe(name='relic name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def relics(self, interaction: discord.Interaction, name: str):

        '''
        Relics (aka Gadgets) are tools that aid the player in exploration or combat.
        '''

        await interaction.response.defer()

        relic = await get_relic(name=name)
        
        await interaction.edit_original_response(embed=relic.embed, view=RelicView(relic=relic, owner=interaction.user))
    
    @relics.autocomplete(name='name')
    async def relics_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=f'[{relic.rarity}] {relic.name}' if relic.chinaOnly == False else f'[CN] [{relic.rarity}] {relic.name}',
                value=relic.name) 
            for relic in await get_names('relics') if current.lower() in relic.name.lower() and isinstance(relic, Relic)][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(RelicsCog(bot))
