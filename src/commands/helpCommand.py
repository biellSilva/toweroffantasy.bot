import discord

from discord.ext import commands
from discord import app_commands

from src.config import no_bar
from src.views.help_view import NamesView


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

        em = discord.Embed(color=no_bar, 
                           title=f'{self.bot.user.name} Help Panel',
                           description='')
        
        tree = self.bot.tree
        commands_ = await tree.fetch_commands()
        
        for command in commands_:
            if command.name == 'help':
                continue

            em.description += (f"{command.mention}\n"
                               f"*{command.description}*\n\n")

        await interaction.edit_original_response(embed=em, view=NamesView())
    
async def setup(bot):
    await bot.add_cog(Help_command(bot))
