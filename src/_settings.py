from typing import Literal

from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    ENV: Literal["prod", "dev"] = "dev"

    API_URL: str = "http://localhost:8000"

    DISCORD_CLIENT_ID: str | None = None
    DISCORD_PUBLIC_KEY: str | None = None
    DISCORD_BOT_TOKEN: str

    WEBSITE_URL: str = "https://toweroffantasy.info"


config = _Settings()  # type: ignore

__all__ = ("config",)
