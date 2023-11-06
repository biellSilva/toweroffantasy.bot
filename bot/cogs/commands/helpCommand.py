import discord

from discord.ext import commands
from discord import app_commands

from bot.core.views.help_view import NamesView
from bot.utils import get_ratelimit
from bot.core.controller.get_data import get_names


class HelpCog(commands.Cog):

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

        em = discord.Embed(color=discord.Colour.dark_embed(),
                            title=f'{self.bot.user.name} Help' if self.bot.user else 'Help',
                            description=f'Status: **{self.bot.status}** \n'
                                        f'Latency: **{round(self.bot.latency * 1000)}ms**\n'
                                        f'Working on **{len(self.bot.guilds)} Guilds**')
        
        em.add_field(name='Git Status', value=(f'> Limit: *{git_api.get("limit")}*\n'
                                               f'> Remain: *{git_api.get("remaining")}*\n'
                                               f'> Used: *{git_api.get("used")}*\n'
                                               f'> Reset: <t:{git_api.get("reset")}:R>\n'), inline=False)

        x = (f'> Simulacras: *{len(await get_names("simulacras"))} itens*\n'
             f'> Matrices: *{len(await get_names("matrices"))} itens*\n'
             f'> Relics: *{len(await get_names("relics"))} itens*\n'
             f'> Mounts: *{len(await get_names("mounts"))} itens*\n'
             f'> Smart Servants: *{len(await get_names("smart-servants"))} itens*\n')

        em.add_field(name='Data', value=x, inline=False)

        await interaction.edit_original_response(embed=em, view=NamesView())
    
async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))
