import discord
import traceback

from discord.ext import commands
from discord import app_commands

from traceback import print_exception
from sys import stderr
from time import time
from typing import Union

from src.errorHandler.customErrors import DataNotFound


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
    async def on_app_command_completion(self, interaction: discord.Interaction, command: Union[app_commands.Command, app_commands.ContextMenu]):

        # For Data Analysis purposes

        print(f'Command: /{command.name}\n'
              f'User: {interaction.user}\n'
              f'Guild: {interaction.guild}\n'
              )

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction: discord.Interaction, err):

        em = discord.Embed(color=discord.Colour.dark_red())
        
        if isinstance(err, app_commands.CommandInvokeError):
            err = err.original

        if isinstance(err, app_commands.CommandNotFound):
            return

        elif isinstance(err, app_commands.MissingPermissions):
            em.description='Missing permission' + '\n'.join(err.args)

        elif isinstance(err, app_commands.MissingRole):
            em.description=f'Missing role {interaction.guild.get_role(int(err.missing_role)).mention}'
        
        elif isinstance(err, app_commands.BotMissingPermissions):
            em.description='\n'.join(err.args)

        elif isinstance(err, DataNotFound):
            em.description = err.message

        elif isinstance(err, app_commands.CommandOnCooldown):
            em.description = (f'Command on cooldown **`{int(err.cooldown.per)} seconds`**\n'
                              f'Try again <t:{int(time() + err.retry_after)}:R>')

        elif isinstance(err, NotImplementedError):
            em.description = f'Not implemented yet'

        elif isinstance(err, discord.Forbidden):
            if err.code == 50007:
                em.description = 'I can\'t send DM\'s to you, try allowing to receive DM\'s from here'


        if em.description and interaction.response.is_done():
            await interaction.edit_original_response(embed=em)
        elif em.description and not interaction.response.is_done():
            await interaction.response.send_message(embed=em, ephemeral=True)
        else:
            txt_err = ''.join(traceback.format_exception(type(err), err, err.__traceback__))
            txt_err = f'```{txt_err}```'
            if len(txt_err) < 2000:
                await self.bot.application.owner.send(txt_err)
            else:
                await self.bot.application.owner.send(f'```Error\n{err}```')

            print(file=stderr)
            print_exception(type(err), err, err.__traceback__, file=stderr)


async def setup(bot: commands.Bot):
    await bot.add_cog(AppErrorHandler(bot))