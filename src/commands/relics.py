import discord

from discord.ext import commands
from discord import app_commands

from src.config import base_url_dict
from src.views.relic_view import RelicView
from src.controller.get_data import get_relic, get_names
from src.models import Relic


class Relics(commands.Cog):

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

        CN_tag = '' if not relic.chinaOnly else '[CN]'

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{relic.name} {relic.rarity} {CN_tag}',
                           description=relic.description)
        
        em.set_thumbnail(url=relic.imgSrc)
        
        if 'overdrive' in relic.name.lower():
            em.url = base_url_dict['relics_home'] + 'booster-shot'
        else:
            em.url = base_url_dict['relics_home'] + relic.name.replace(' ', '-').lower()
        
        await interaction.edit_original_response(embed=em, view=RelicView(relic=relic))
    
    @relics.autocomplete(name='name')
    async def relics_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice]:
        relics_: list[Relic] = await get_names('relics')
        return [
            app_commands.Choice(
                name=f'{relic.name} {relic.rarity}' if relic.chinaOnly == False else f'{relic.name} {relic.rarity} [CN]',
                value=relic.name) 
            for relic in relics_ if current.lower() in relic.name.lower()][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Relics(bot))
