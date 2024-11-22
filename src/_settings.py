from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    API_URL: str = "http://localhost:8000"

    DISCORD_CLIENT_ID: str | None = None
    DISCORD_PUBLIC_KEY: str | None = None
    DISCORD_TOKEN: str | None = None


config = _Settings()

__all__ = ("config",)
