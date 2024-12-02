from abc import abstractmethod
from datetime import timedelta
from typing import Self

import aiohttp
from cachetools import TTLCache
from pydantic import BaseModel

from src._settings import config
from src.types import LangsEnum


class ApiBaseService[T: BaseModel]:
    __instance: Self | None = None

    def __new__(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self._cache = TTLCache[LangsEnum, dict[str, T]](
            maxsize=100, ttl=timedelta(hours=1).total_seconds()
        )

    @staticmethod
    def _get_client() -> aiohttp.ClientSession:
        return aiohttp.ClientSession(config.API_URL)

    @abstractmethod
    async def _update_cache(self, lang: LangsEnum) -> None:
        pass

    async def clear_cache(self) -> None:
        self._cache.clear()

    async def _get_lang_from_cache(self, lang: LangsEnum) -> dict[str, T]:
        if lang not in self._cache:
            await self._update_cache(lang)
        return self._cache[lang]

    async def get_all_from_cache(self, lang: LangsEnum) -> list[T]:
        return list((await self._get_lang_from_cache(lang)).values())
