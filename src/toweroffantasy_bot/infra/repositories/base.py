import inspect
from abc import ABC, abstractmethod
from typing import Generic, Type, TypeVar, get_args, get_type_hints

from adapters.api.client import ApiClient
from domain.models.base import EntityBase
from pydantic import BaseModel

BM = TypeVar("BM", bound=EntityBase)
BMS = TypeVar("BMS", bound=EntityBase)


class BaseRepository(ABC, Generic[BMS, BM]):

    def __init__(self) -> None:
        self.client = ApiClient.get_instance()
        self.model_simple = BMS
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

    @abstractmethod
    async def get_simple(self, id: str, lang: str, version: str) -> BMS: ...

    @abstractmethod
    async def get(self, id: str, lang: str, version: str) -> BM: ...

    @abstractmethod
    async def get_all_simple(self, lang: str, version: str) -> list[BMS]: ...

    @abstractmethod
    async def get_all(self, lang: str, version: str) -> list[BM]: ...
