from logging import getLogger

import discord
from discord.ext import commands, tasks

from src._settings import config

_logger = getLogger("tof.tasks.update_presence")


class UpdatePresenceCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def on_load(self) -> None:
        await self.bot.wait_until_ready()
        self.update_presence.start()
        _logger.debug("Update presence task started")

    async def on_unload(self) -> None:
        self.update_presence.cancel()

        if self.update_presence.is_running():
            self.update_presence.stop()

        _logger.debug("Cache data task stopped")

    @tasks.loop(hours=1)
    async def update_presence(self) -> None:
        activity = discord.Activity(name="Dev", type=discord.ActivityType.playing)
        status = discord.Status.do_not_disturb

        if config.ENV != "dev":
            from src.api._base import ApiService

            activity = discord.Activity(
                name=(await ApiService().get_version()).game_version,
                type=discord.ActivityType.playing,
            )
            status = discord.Status.online

        await self.bot.change_presence(activity=activity, status=status)

        _logger.info("Bot presence changed: %s | %s", activity.name, status.name)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UpdatePresenceCog(bot=bot))
