
import os
import logging
import discord

from discord.ext import commands


_log_extension = logging.getLogger('tof_info.extension')


async def load_cogs_by_dir(bot: commands.Bot, dir: str = 'bot/cogs') -> None:
    
    for filename in os.listdir(dir):
        if filename == '__pycache__':
            continue
        
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"{dir}.{filename[:-3]}".replace('/', '.'))
                _log_extension.info(f"{dir.rsplit('/', 1)[1]}.{filename[:-3]} loaded")

            except commands.NoEntryPointError:
                pass
    
        if os.path.isdir(path := f"{dir}/{filename}"):
            await load_cogs_by_dir(bot, path)


async def wait_until_ready_tasks(bot: commands.Bot, maintenance: bool = False):
        await bot.wait_until_ready()

        if maintenance:
            await bot.change_presence(activity=discord.Activity(
                        type=discord.ActivityType.listening,
                        name='MAINTENANCE'),
                        status=discord.Status.dnd
                        )
        else:
            await bot.change_presence(activity=discord.Activity(
                        type=discord.ActivityType.listening,
                        name='/help'),
                        status=discord.Status.online
                        )