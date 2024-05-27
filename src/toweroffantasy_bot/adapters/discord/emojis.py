from discord import Emoji
from discord.ext import commands
from settings import config


class BotEmojis:
    _emojis: dict[str, Emoji] = {}

    @classmethod
    async def load_emojis(cls, bot: commands.Bot) -> None:
        await bot.wait_until_ready()

        if guild := bot.get_guild(config.default_guild_id):
            for emoji in guild.emojis:
                cls._emojis[emoji.name] = emoji

            if not cls._emojis:
                raise ValueError("No emojis found")

        else:
            raise ValueError("Guild not found")

    @classmethod
    def get(cls, name: str) -> Emoji:
        if not cls._emojis:
            raise ValueError("Emojis not loaded")

        if name not in cls._emojis:
            raise ValueError(f"Emoji {name} not found")

        return cls._emojis[name]

    @classmethod
    def get_str(cls, name: str) -> str:
        emoji = cls.get(name)
        return f"<:{emoji.name}:{emoji.id}>"
