import logging
from pathlib import Path

import discord
from discord import Locale
from discord.ext import commands
from settings import config

from .emojis import BotEmojis


async def load_cogs(
    bot: commands.Bot, path: Path = Path("src/toweroffantasy_bot/adapters/discord/cogs")
) -> None:
    logger_extension = logging.getLogger("tof.extension")

    for item in path.iterdir():

        if item.is_dir():
            await load_cogs(bot, item)
            continue

        if item.suffix == ".py":
            logger_extension.debug(f"Loading {str(item)}")

            cog_name = ".".join(str(item).split("\\")[2:]).removesuffix(
                ".py"
            ) or ".".join(str(item).split("/")[2:]).removesuffix(".py")

            try:
                await bot.load_extension(cog_name)
            except (
                commands.errors.ExtensionNotFound,
                commands.errors.NoEntryPointError,
            ):
                continue

            logger_extension.info(f"Loaded {cog_name.split('.')[-1].title()}Cog")


async def wait_until_ready_tasks(bot: commands.Bot) -> None:

    await bot.wait_until_ready()

    logger_client = logging.getLogger("tof.client")

    async def being_remade():
        status = discord.Status.online
        activity_text = "v4.0 Ready"
        await bot.change_presence(
            status=status, activity=discord.Game(name=activity_text)
        )
        logger_client.info(
            f'Changed presence to "{activity_text}" with status {status}'
        )

    async def load_emojis():
        await BotEmojis.load_emojis(bot=bot)

    await being_remade()
    await load_emojis()


def rarity_to_stars(rarity: int) -> str:
    return config.star_str * rarity


def rarity_to_string(rarity: int) -> str:
    match rarity:
        case 2:
            return "N"

        case 3:
            return "R"

        case 4:
            return "SR"

        case 5:
            return "SSR"

        case 6:
            return "SSR+"

        case _:
            return "N-"


def convert_locale(locale: Locale) -> str:
    match locale:
        case lang if lang in (
            Locale.american_english,
            Locale.british_english,
        ):
            return "en"

        case lang if lang in (Locale.brazil_portuguese,):
            return "pt"

        case lang if lang in (Locale.spain_spanish,):
            return "es"

        case lang if lang in (Locale.french,):
            return "fr"

        case lang if lang in (Locale.indonesian,):
            return "id"

        case lang if lang in (Locale.japanese,):
            return "ja"

        case lang if lang in (Locale.russian,):
            return "ru"

        case lang if lang in (Locale.german,):
            return "de"

        case lang if lang in (Locale.thai,):
            return "th"

        case lang if lang in (Locale.chinese, Locale.taiwan_chinese):
            return "zh-cn"

        case _:
            return "en"
