from discord import Locale

from src.api._base import ApiBaseService
from src.models.weapons import Weapon, WeaponSimple
from src.types import LangsEnum
from src.utils import convert_locale


class WeaponService(ApiBaseService[WeaponSimple]):
    _PATH = "/weapons"

    async def _update_cache(self, lang: LangsEnum) -> None:
        async with self._get_client() as client:
            async with client.get(self._PATH, params={"lang": lang}) as response:
                data = [WeaponSimple(**data) for data in await response.json()]
                self._cache[lang] = {data.id: data for data in data}

    async def get_id(self, lang: Locale, id_: str) -> Weapon:
        async with self._get_client() as client:
            async with client.get(
                f"{self._PATH}/{id_}", params={"lang": convert_locale(lang)}
            ) as response:
                return Weapon(**await response.json())

    async def get_all(self, lang: Locale) -> list[WeaponSimple]:
        async with self._get_client() as client:
            async with client.get(
                self._PATH, params={"lang": convert_locale(lang)}
            ) as response:
                return [WeaponSimple(**data) for data in await response.json()]
