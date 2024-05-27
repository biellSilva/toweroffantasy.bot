from adapters.discord.bot import TofBot
from logger import setup_logging
from settings import config

if __name__ == "__main__":
    setup_logging()

    bot = TofBot()
    bot.run(token=config.TOKEN)
