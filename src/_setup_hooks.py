from logging import getLogger
from pathlib import Path

import discord
from discord.ext import commands


async def load_cogs(bot: commands.Bot) -> None:
    _logger = getLogger("tof.extensions")

    async def path_loader(path: str = "./src/cogs") -> None:
        for file in Path(path).iterdir():
            if "__pycache__" in file.parts:
                continue

            if (
                file.is_file()
                and file.with_suffix(".py")
                and file.name != "__init__.py"
            ):
                cog_path = ".".join(file.parts).removesuffix(".py")
                cog_short_path = ".".join(file.parts[2:]).removesuffix(".py")
                _logger.debug(f"Loading extension {cog_path}")

                try:
                    await bot.load_extension(cog_path)
                except commands.NoEntryPointError:
                    _logger.warning(f"Extension {cog_short_path} has no setup function")
                    continue

                _logger.info(f"Loaded extension {cog_short_path}")

            elif file.is_dir():
                _logger.debug(f"Loading extensions from {file}")

                await path_loader(str(file))

    await path_loader()


async def change_presence(bot: commands.Bot) -> None:
    _logger = getLogger("tof.presence")

    await bot.wait_until_ready()

    await bot.change_presence(
        activity=discord.CustomActivity(
            name="being developed",
            emoji="🛠️",
        ),
        status=discord.Status.dnd,
    )

    _logger.info("Bot presence changed")
