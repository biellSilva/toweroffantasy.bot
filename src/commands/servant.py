import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar, emojis_1
from src.utils import get_git_data, get_image
from src.views.servant_view import ServantView


class Servants(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='servants')
    @app_commands.describe(name='Servant name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    @app_commands.checks.cooldown(1, 30, key=lambda i: i.user.id)
    async def servant(self, interaction: discord.Interaction, name: str):

        '''
        Smart Servants are small robots that aid the player in combat.
        '''

        await interaction.response.defer()

        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')
        thumb_url = await get_image(name=servant['imgSrc'], data='smart-servants')

        em = discord.Embed(color=no_bar, 
                           title=f'{servant["name"]}' if 'chinaOnly' not in servant else f'{servant["name"]} [CN]',
                           description=f"{emojis_1[servant['type']]} {emojis_1[servant['element']]}\n"
                                       f"Attack: **{servant['attack']}** \n"
                                       f"Crit: **{servant['crit']}** \n\n"
                                       f"{servant['description']}")

        if thumb_url:
            em.set_thumbnail(url=thumb_url)

        await interaction.edit_original_response(embed=em, view=ServantView())

    
async def setup(bot):
    await bot.add_cog(Servants(bot))
