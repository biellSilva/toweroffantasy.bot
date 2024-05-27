from domain.models.weapons import WeaponSimple
from gql import gql

from .base import BaseCache


class WeaponCache(BaseCache[WeaponSimple]):

    async def _load_lang(self, lang: str, version: str) -> None:
        query = (
            "query GetAllSimple($lang: String!, $version: String!) {"
            "weapons(lang: $lang, version: $version) {"
            f"{await self.get_fields(WeaponSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )

            if version not in self._cache:
                self._cache[version] = {}

            self._cache[version][lang] = [
                WeaponSimple(**data) for data in result["weapons"]
            ]
