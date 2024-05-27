import logging

import discord
from discord.ext import commands
from settings import config

logger_client = logging.getLogger("tof.client")


class TofBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=config.command_prefix,
            intents=discord.Intents.all(),
            case_insensitive=True,
            strip_after_prefix=True,
            help_command=None,
        )

    async def on_ready(self) -> None:
        """
        On ready event handler

        this should not be used for anything other than logging on_ready
        """

        logger_client.info(
            f"{self.user} - {self.status} - {round(self.latency*1000)}ms"
        )

    async def setup_hook(self) -> None:
        """
        Setup hook occurs before the bot is ready

        This is where we load cogs and other tasks
        that need to be done before the bot is ready
        such as changing presence, connecting to databases etc
        """

        from adapters.discord.utils import (
            load_cogs,
            wait_until_ready_tasks,
        )

        self.loop.create_task(wait_until_ready_tasks(self))

        await load_cogs(self)
