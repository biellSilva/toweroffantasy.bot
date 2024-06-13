from gql import gql
from infra.repositories.base import BaseRepository
from domain.models.mounts import MountSimple, Mount


class MountsRepository(BaseRepository[MountSimple, Mount]):

    async def get_simple(self, id: str, lang: str, version: str) -> MountSimple:
        query = (
            "query GetSimple($id: String!, $lang: String!, $version: String!) {"
            "mount(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(MountSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return MountSimple(**result["mount"])

    async def get_all_simple(self, lang: str, version: str) -> list[MountSimple]:

        query = (
            "query GetAllSimple($lang: String!, $version: String!) {"
            "mounts(lang: $lang, version: $version) {"
            f"{await self.get_fields(MountSimple)}"
            "}}"
        )
        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [MountSimple(**data) for data in result["mounts"]]

    async def get(self, id: str, lang: str, version: str) -> Mount:
        query = (
            "query GetFull($id: String!, $lang: String!, $version: String!) {"
            "mount(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(Mount)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return Mount(**result["mount"])

    async def get_all(self, lang: str, version: str) -> list[Mount]:
        query = (
            "query GetAllFull($lang: String!, $version: String!) {"
            "mounts(lang: $lang, version: $version) {"
            f"{await self.get_fields(Mount)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [Mount(**data) for data in result["mounts"]]
