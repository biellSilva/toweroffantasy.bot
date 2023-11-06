import discord
import logging

from discord.ext import commands
from discord import app_commands

from time import time
from typing import Union, Any

from bot.cogs.errorHandler.customErrors import *

_log_error = logging.getLogger('tof_info.error')
_log_command = logging.getLogger('tof_info.command')


class AppErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        tree = self.bot.tree
        self._old_tree_error = tree.on_error
        tree.on_error = self.on_app_command_error

    async def cog_unload(self):
        tree = self.bot.tree
        tree.on_error = self._old_tree_error

    @commands.Cog.listener()
    async def on_app_command_completion(self, interaction: discord.Interaction, command: Union[app_commands.Command[Any, Any, Any], app_commands.ContextMenu]):

        # For debug purposes

        _log_command.debug(f'Command: /{command.qualified_name}\t User: {interaction.user}\t Guild: {interaction.guild}')


    @commands.Cog.listener()
    async def on_app_command_error(self, interaction: discord.Interaction, err: Exception):

        em = discord.Embed(color=discord.Colour.dark_red())
        
        if isinstance(err, app_commands.CommandInvokeError):
            err = err.original

        if isinstance(err, app_commands.CommandNotFound):
            return

        elif isinstance(err, app_commands.MissingPermissions):
            em.description='Missing permission' + '\n'.join(err.args)

        elif isinstance(err, app_commands.MissingRole):
            em.description=f'Missing role <@&{err.missing_role}>'
        
        elif isinstance(err, app_commands.BotMissingPermissions):
            em.description='\n'.join(err.args)

        elif isinstance(err, DataNotFound):
            em.description = err.message
        
        elif isinstance(err, WrongDatetimeFormat):
            em.description = err.message

        elif isinstance(err, app_commands.CommandOnCooldown):
            em.description = f'Cooldown **<t:{int(time() + err.retry_after)}:R>**'

        elif isinstance(err, NotImplementedError):
            em.description = f'Not implemented yet'

        elif isinstance(err, discord.Forbidden):
            if err.code == 50007:
                em.description = 'I can\'t send DM\'s to you, try allowing to receive DM\'s from here'


        if em.description and interaction.response.is_done():
            await interaction.followup.send(embed=em, ephemeral=True)

        elif em.description and not interaction.response.is_done():
            await interaction.response.send_message(embed=em, ephemeral=True)

        else:
            _log_error.error(f'Ignoring exception in command {interaction.command} for {interaction.user} in {interaction.guild}', exc_info=err)

            em.description = 'An error has occurred'

            if interaction.response.is_done():
                await interaction.followup.send(embed=em, ephemeral=True)
            else:
                await interaction.response.send_message(embed=em, ephemeral=True)

            if self.bot.application:
                await self.bot.application.owner.send(f'```Error\n{err}```')



async def setup(bot: commands.Bot):
    await bot.add_cog(AppErrorHandler(bot))