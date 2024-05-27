from domain.models.weapons import Weapon, WeaponSimple
from gql import gql
from infra.repositories.base import BaseRepository


class WeaponRepository(BaseRepository[WeaponSimple, Weapon]):

    async def get_simple(self, id: str, lang: str, version: str) -> WeaponSimple:
        query = (
            "query GetSimple($id: String!, $lang: String!, $version: String!) {"
            "weapon(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(WeaponSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return WeaponSimple(**result["weapon"])

    async def get_all_simple(self, lang: str, version: str) -> list[WeaponSimple]:

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
            return [WeaponSimple(**data) for data in result["weapon"]]

    async def get(self, id: str, lang: str, version: str) -> Weapon:
        query = (
            "query GetFull($id: String!, $lang: String!, $version: String!) {"
            "weapon(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(Weapon)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return Weapon(**result["weapon"])

    async def get_all(self, lang: str, version: str) -> list[Weapon]:
        query = (
            "query GetAllFull($lang: String!, $version: String!) {"
            "weapons(lang: $lang, version: $version) {"
            f"{await self.get_fields(Weapon)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [Weapon(**data) for data in result["weapon"]]
