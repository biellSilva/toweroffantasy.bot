from src._settings import config

if __name__ == "__main__":
    from src.bot import Bot

    BOT = Bot()

    BOT.run(token=config.DISCORD_TOKEN)
