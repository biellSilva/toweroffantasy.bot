from datetime import timedelta
from typing import Any, Self, overload

import aiohttp
from cachetools import TTLCache
from discord import Locale

from src._settings import config
from src.models.base import BaseEntity
from src.types import LangsEnum
from src.utils import convert_locale


class ApiBaseService[T: BaseEntity, B: BaseEntity]:
    __instance: Self | None = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, *, model: type[T], simple_model: type[B], path: str) -> None:
        self._model = model
        self._simple_model = simple_model
        self._PATH = path
        self._cache = TTLCache[LangsEnum, dict[str, B]](
            maxsize=100, ttl=timedelta(hours=1).total_seconds()
        )

    @staticmethod
    def _get_client() -> aiohttp.ClientSession:
        return aiohttp.ClientSession(config.API_URL)

    def clear_cache(self) -> None:
        self._cache.clear()

    async def _get_lang_from_cache(self, lang: LangsEnum) -> dict[str, B]:
        if lang not in self._cache:
            await self._update_cache(lang)
        return self._cache[lang]

    async def get_all_from_cache(self, lang: LangsEnum) -> list[B]:
        return list((await self._get_lang_from_cache(lang)).values())

    @overload
    async def _process_request(self, lang: LangsEnum) -> list[T]: ...

    @overload
    async def _process_request(self, lang: LangsEnum, id_: str) -> T: ...

    async def _process_request(
        self, lang: LangsEnum, id_: str | None = None
    ) -> T | list[T]:
        async with self._get_client() as client:
            if id_ is None:
                async with client.get(self._PATH, params={"lang": lang}) as response:
                    return [self._model(**data) for data in await response.json()]

            async with client.get(
                f"{self._PATH}/{id_}", params={"lang": lang}
            ) as response:
                return self._model(**await response.json())

    async def _validate_request(self, response: aiohttp.ClientResponse) -> None:
        if response.status != 200:
            msg = await response.text() or "No message"
            raise Exception(f"Status code: {response.status}, message: {msg}")

    async def _update_cache(self, lang: LangsEnum) -> None:
        data = await self.get_all(lang, 1, 1000)
        self._cache[lang] = {data.id: data for data in data}

    def _clear_query_params(self, query_params: dict[str, Any]) -> dict[str, Any]:
        return {key: value for key, value in query_params.items() if value is not None}

    async def get_id(self, lang: Locale, id_: str) -> T:
        return await self._process_request(convert_locale(lang), id_)

    async def get_all(
        self,
        lang: Locale | LangsEnum,
        page: int = 1,
        limit: int = 1000,
        **query_params: Any,
    ) -> list[B]:
        async with self._get_client() as client:
            async with client.get(
                self._PATH,
                params={
                    "lang": convert_locale(lang),
                    "page": page,
                    "limit": limit,
                    **self._clear_query_params(query_params),
                },
            ) as response:
                print(response.real_url)
                return [self._simple_model(**data) for data in await response.json()]

    async def fetch_autocomplete_data(
        self,
        lang: Locale,
        page: int = 1,
        limit: int = 1000,
        **query_params: Any,
    ) -> list[B]:
        async with self._get_client() as client:
            async with client.get(
                self._PATH,
                params={
                    "lang": convert_locale(lang),
                    "page": page,
                    "limit": limit,
                    **self._clear_query_params(query_params),
                },
            ) as response:
                print(response.real_url)
                return [self._simple_model(**data) for data in await response.json()]
