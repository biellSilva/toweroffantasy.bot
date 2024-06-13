from domain.models.relics import Relic, RelicSimple
from gql import gql
from infra.repositories.base import BaseRepository


class RelicsRepository(BaseRepository[RelicSimple, Relic]):

    async def get_simple(self, id: str, lang: str, version: str) -> RelicSimple:
        query = (
            "query GetSimple($id: String!, $lang: String!, $version: String!) {"
            "relic(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(RelicSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return RelicSimple(**result["relic"])

    async def get_all_simple(self, lang: str, version: str) -> list[RelicSimple]:

        query = (
            "query GetAllSimple($lang: String!, $version: String!) {"
            "relics(lang: $lang, version: $version) {"
            f"{await self.get_fields(RelicSimple)}"
            "}}"
        )
        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [RelicSimple(**data) for data in result["relics"]]

    async def get(self, id: str, lang: str, version: str) -> Relic:
        query = (
            "query GetFull($id: String!, $lang: String!, $version: String!) {"
            "relic(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(Relic)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return Relic(**result["relic"])

    async def get_all(self, lang: str, version: str) -> list[Relic]:
        query = (
            "query GetAllFull($lang: String!, $version: String!) {"
            "relics(lang: $lang, version: $version) {"
            f"{await self.get_fields(Relic)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [Relic(**data) for data in result["relics"]]
