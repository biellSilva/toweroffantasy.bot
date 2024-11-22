from discord import Locale

from src.api._base import ApiBaseService
from src.models.imitation import Imitation
from src.types import LangsEnum
from src.utils import convert_locale


class SimulacraService(ApiBaseService[Imitation]):
    _PATH = "/simulacra"

    async def _update_cache(self, lang: LangsEnum) -> None:
        async with self._get_client() as client:
            async with client.get(self._PATH, params={"lang": lang}) as response:
                data = [Imitation(**data) for data in await response.json()]
                self._cache[lang] = {data.id: data for data in data}

    async def get_id(self, lang: Locale, id_: str) -> Imitation:
        async with self._get_client() as client:
            async with client.get(
                f"{self._PATH}/{id_}", params={"lang": convert_locale(lang)}
            ) as response:
                return Imitation(**await response.json())

    async def get_all(self, lang: Locale) -> list[Imitation]:
        async with self._get_client() as client:
            async with client.get(
                self._PATH, params={"lang": convert_locale(lang)}
            ) as response:
                return [Imitation(**data) for data in await response.json()]
