from domain.models.matrices import MatrixSimple
from gql import gql

from .base import BaseCache


class WeaponCache(BaseCache[MatrixSimple]):

    async def _load_lang(self, lang: str, version: str) -> None:
        query = (
            "query GetAllSimple($lang: String!, $version: String!) {"
            "matrices(lang: $lang, version: $version) {"
            f"{await self.get_fields(MatrixSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )

            if version not in self._cache:
                self._cache[version] = {}

            self._cache[version][lang] = [
                MatrixSimple(**data) for data in result["matrices"]
            ]
