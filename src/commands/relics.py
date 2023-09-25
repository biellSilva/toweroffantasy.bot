import discord

from discord.ext import commands
from discord import app_commands

from src.config import base_url_dict
from src.utils import get_git_data, get_image
from src.views.relic_view import RelicView


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

        relic: dict = await get_git_data(name=name, data_folder='relics', data_type='json')
        thumb_url = await get_image(name=relic['imgSrc'], data='relics')

        CN_tag = '' if 'chinaOnly' not in relic or not relic['chinaOnly'] else '[CN]'

        em = discord.Embed(color=discord.Colour.dark_embed(), 
                           title=f'{relic["name"]} {relic["rarity"]} {CN_tag}',
                           description=relic['description'])
        
        if 'overdrive' in relic['name'].lower():
            em.url = base_url_dict['relics_home'] + 'booster-shot'
        else:
            em.url = base_url_dict['relics_home'] + relic['name'].replace(' ', '-').lower()
        
        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em, view=RelicView())
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Relics(bot))
