from logging import getLogger

from discord import Intents
from discord.app_commands.installs import AppCommandContext, AppInstallationType
from discord.ext import commands

from src import _setup_hooks
from src._logging import setup_logging as _setup_logging
from src._settings import config

_setup_logging()


class Bot(commands.Bot):
    """Custom bot class."""

    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned,
            allowed_contexts=AppCommandContext(
                guild=True, dm_channel=True, private_channel=True
            ),
            allowed_installs=AppInstallationType(guild=True, user=True),
            intents=Intents.default(),
        )

    async def on_ready(self) -> None:
        """Event that is called when the bot is ready."""

        logger = getLogger("tof.client")
        logger.info("Logged in as %s | %sms", self.user, round(self.latency * 1000, 1))

    async def setup_hook(self) -> None:
        """Hook for setting up the bot."""

        await _setup_hooks.load_cogs(self)

        self.loop.create_task(_setup_hooks.change_presence(self))

    def init(self) -> None:
        """Initialize the bot."""

        self.run(token=config.DISCORD_BOT_TOKEN)
