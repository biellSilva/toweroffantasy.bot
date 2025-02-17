from discord import Locale

from src.api._base import ApiBaseService
from src.models.weapons import Weapon, WeaponSimple
from src.utils import convert_locale


class WeaponService(ApiBaseService[WeaponSimple]):
    _PATH = "/weapons"

    def __init__(self) -> None:
        super().__init__(model=WeaponSimple, path=self._PATH)

    async def get_id(self, lang: Locale, id_: str) -> Weapon:
        async with self._get_client() as client:
            async with client.get(
                f"{self._PATH}/{id_}", params={"lang": convert_locale(lang)}
            ) as response:
                return Weapon(**await response.json())
