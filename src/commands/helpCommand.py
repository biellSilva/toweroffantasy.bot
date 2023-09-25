import discord

from discord.ext import commands
from discord import app_commands
from time import time

from src.views.help_view import NamesView
from src.utils import data_base, get_ratelimit, get_git_data, get_image


class Help_command(commands.Cog):

    '''Help Command'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name='help')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    @app_commands.checks.cooldown(1, 30, key=lambda i: i.user.id)
    async def my_help_command(self, interaction: discord.Interaction):

        '''
        Contains information that may help you.
        '''

        await interaction.response.defer()

        git_api = await get_ratelimit()

        start_data_timer = time()
        await get_git_data('Yu lan', 'weapons', data_type='json')
        get_data_timer = time() - start_data_timer

        start_image_timer = time()
        await get_image(name=('Yu lan', 'yulan'), data='simulacra')
        get_image_timer = time() - start_image_timer

        em = discord.Embed(color=discord.Colour.dark_embed(),
                            title=f'{self.bot.user.name} Help',
                            description=f'Status: **{self.bot.status}** \n'
                                        f'Latency: **{round(self.bot.latency * 1000)}ms**\n'
                                        f'Data Latency: **{round(get_data_timer * 1000)}ms**\n'
                                        f'Image Latency: **{round(get_image_timer * 1000)}ms**\n'
                                        f'Working on **{len(self.bot.guilds)} Guilds**')
        
        em.add_field(name='Git Status', value=(f'> Limit: *{git_api.get("limit")}*\n'
                                               f'> Remain: *{git_api.get("remaining")}*\n'
                                               f'> Used: *{git_api.get("used")}*\n'
                                               f'> Reset: <t:{git_api.get("reset")}:R>\n'), inline=False)

        x = ''
        for data_folder, data_list in data_base.items():
            x += f'> {data_folder.title()}: *{len(data_list)} itens*\n' 

        em.add_field(name='Data', value=x, inline=False)

        await interaction.edit_original_response(embed=em, view=NamesView())
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Help_command(bot))
