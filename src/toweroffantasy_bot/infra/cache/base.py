import inspect
from abc import ABC, abstractmethod
from typing import Generic, Type, TypeVar, get_args, get_type_hints

from adapters.api.client import ApiClient
from domain.models.base import EntityBase
from pydantic import BaseModel

BM = TypeVar("BM", bound=EntityBase)


class BaseCache(ABC, Generic[BM]):

    _cache: dict[str, dict[str, list[BM]]] = {}
    """
    Cache version -> lang -> list[BM]
    """

    def __init__(self) -> None:
        self.client = ApiClient.get_instance()
        self.model = BM

    async def get_fields(self, model: Type[BaseModel]) -> str:
        fields = ""

        for field, field_type in get_type_hints(model, include_extras=True).items():
            fields += f"{field} "

            for arg in get_args(field_type):
                if inspect.isclass(arg) and issubclass(arg, BaseModel):
                    fields += "{ " + await self.get_fields(arg) + " }"

            if inspect.isclass(field_type) and issubclass(field_type, BaseModel):
                fields += "{ " + await self.get_fields(field_type) + " }"

        return fields

    async def load_global(self) -> None:
        for lang in [
            "de",
            "en",
            "es",
            "fr",
            "id",
            "ja",
            "pt",
            "ru",
            "th",
            "zh-cn",
        ]:
            await self._load_lang(lang, "global")

    async def load_china(self) -> None:
        for lang in [
            "cn",
        ]:
            await self._load_lang(lang, "china")

    async def load_all(self) -> None:
        await self.load_global()
        await self.load_china()

    async def get_lang(self, lang: str, version: str) -> list[BM]:
        if version not in self._cache:
            await self._load_lang(lang, version)

        return self._cache[version][lang]

    @abstractmethod
    async def _load_lang(self, lang: str, version: str) -> None: ...
