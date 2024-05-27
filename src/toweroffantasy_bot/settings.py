from datetime import datetime

from pydantic_settings import BaseSettings
from pytz import timezone


class _Settings(BaseSettings):
    TOKEN: str
    "Discord bot token (required)"

    command_prefix: str = "t!"
    "Command prefix (default: t!)"

    last_restart: datetime = datetime.now(tz=timezone("UTC"))
    "Last time the bot was restarted"

    tof_info_url: str = "https://toweroffantasy.info"

    default_guild_id: int = 1000974290801410138


config = _Settings()  # type: ignore
