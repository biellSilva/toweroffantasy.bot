import discord
import traceback

from discord.ext import commands
from discord import app_commands
from discord.app_commands import AppCommandError

from traceback import print_exception
from sys import stderr
from time import time

from src.config import no_bar


class AppErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def cog_load(self):
        tree = self.bot.tree
        self._old_tree_error = tree.on_error
        tree.on_error = self.on_app_command_error

    def cog_unload(self):
        tree = self.bot.tree
        tree.on_error = self._old_tree_error

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction: discord.Interaction, err):

        em = discord.Embed(color=no_bar,
                        description='')

        show = False
        
        if isinstance(err, app_commands.CommandInvokeError):
            err = err.original

        if isinstance(err, app_commands.MissingPermissions):
            em.description='Missing permission' + '\n'.join(err.args)

        if isinstance(err, app_commands.MissingRole):
            em.description=f'Missing role {interaction.guild.get_role(int(err.missing_role)).mention}'
        
        if isinstance(err, app_commands.BotMissingPermissions):
            em.description='\n'.join(err.args)
            
        if isinstance(err, (AttributeError, TypeError)):
            em.description = 'Couldn\'t find'
            show = True

        if isinstance(err, app_commands.CommandOnCooldown):
            em.description = (f'Command on Cooldown\n' 
                              f'<t:{int(time() + err.retry_after)}:R>')

        if show:
            print(file=stderr)
            print_exception(type(err), err, err.__traceback__, file=stderr)

        if interaction.response.is_done():
            return await interaction.edit_original_response(embed=em)
        else:
            return await interaction.response.send_message(embed=em, ephemeral=True)


        txt_err = ''.join(traceback.format_exception(type(err), err, err.__traceback__))

        await self.bot.application.owner.send(f'```{txt_err}```')


async def setup(bot):
    await bot.add_cog(AppErrorHandler(bot))