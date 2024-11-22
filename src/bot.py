from logging import getLogger
from typing import Any

from discord import Intents
from discord.app_commands.installs import AppCommandContext, AppInstallationType
from discord.ext import commands

from src import _setup_hooks
from src._logging import setup_logging as _setup_logging

_setup_logging()

_INTENTS = Intents.default()


class Bot(commands.Bot):
    """Custom bot class."""

    def __init__(
        self,
        *,
        description: str | None = None,
        allowed_contexts: AppCommandContext = AppCommandContext(
            guild=True, dm_channel=True, private_channel=True
        ),
        allowed_installs: AppInstallationType = AppInstallationType(
            guild=True, user=True
        ),
        intents: Intents = _INTENTS,
        **options: Any,
    ) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned,
            description=description,
            allowed_contexts=allowed_contexts,
            allowed_installs=allowed_installs,
            intents=intents,
            **options,
        )

    async def on_ready(self) -> None:
        """Event that is called when the bot is ready."""

        logger = getLogger("tof.client")
        logger.info("Logged in as %s", self.user)

    async def setup_hook(self) -> None:
        """Hook for setting up the bot."""

        await _setup_hooks.load_cogs(self)

        self.loop.create_task(_setup_hooks.change_presence(self))
