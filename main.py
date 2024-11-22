from dotenv import find_dotenv

if __name__ == "__main__":
    from dotenv import get_key

    from src.bot import Bot

    BOT = Bot()

    TOKEN = get_key(find_dotenv(), "DISCORD_BOT_TOKEN")

    if not TOKEN:
        raise ValueError("No token found in .env file")

    BOT.run(token=TOKEN)
