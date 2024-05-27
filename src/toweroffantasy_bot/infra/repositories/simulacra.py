from domain.models.simulacra import Simulacra, SimulacraSimple
from gql import gql
from infra.repositories.base import BaseRepository


class SimulacraRepository(BaseRepository[SimulacraSimple, Simulacra]):

    async def get_simple(self, id: str, lang: str, version: str) -> SimulacraSimple:
        query = (
            "query GetSimple($id: String!, $lang: String!, $version: String!) {"
            "simulacrumV2(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(SimulacraSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return SimulacraSimple(**result["simulacrumV2"])

    async def get_all_simple(self, lang: str, version: str) -> list[SimulacraSimple]:

        query = (
            "query GetAllSimple($lang: String!, $version: String!) {"
            "simulacraV2(lang: $lang, version: $version) {"
            f"{await self.get_fields(SimulacraSimple)}"
            "}}"
        )
        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [SimulacraSimple(**simulacra) for simulacra in result["simulacraV2"]]

    async def get(self, id: str, lang: str, version: str) -> Simulacra:
        query = (
            "query GetFull($id: String!, $lang: String!, $version: String!) {"
            "simulacrumV2(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(Simulacra)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return Simulacra(**result["simulacrumV2"])

    async def get_all(self, lang: str, version: str) -> list[Simulacra]:
        query = (
            "query GetAllFull($lang: String!, $version: String!) {"
            "simulacraV2(lang: $lang, version: $version) {"
            f"{await self.get_fields(Simulacra)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [Simulacra(**simulacra) for simulacra in result["simulacraV2"]]
