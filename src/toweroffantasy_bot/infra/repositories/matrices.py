from domain.models.matrices import Matrix, MatrixSimple
from gql import gql
from infra.repositories.base import BaseRepository


class MatricesRepository(BaseRepository[MatrixSimple, Matrix]):

    async def get_simple(self, id: str, lang: str, version: str) -> MatrixSimple:
        query = (
            "query GetSimple($id: String!, $lang: String!, $version: String!) {"
            "matrix(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(MatrixSimple)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return MatrixSimple(**result["matrix"])

    async def get_all_simple(self, lang: str, version: str) -> list[MatrixSimple]:

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
            return [MatrixSimple(**data) for data in result["matrices"]]

    async def get(self, id: str, lang: str, version: str) -> Matrix:
        query = (
            "query GetFull($id: String!, $lang: String!, $version: String!) {"
            "matrix(id: $id, lang: $lang, version: $version) {"
            f"{await self.get_fields(Matrix)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"id": id, "lang": lang, "version": version}
            )
            return Matrix(**result["matrix"])

    async def get_all(self, lang: str, version: str) -> list[Matrix]:
        query = (
            "query GetAllFull($lang: String!, $version: String!) {"
            "matrices(lang: $lang, version: $version) {"
            f"{await self.get_fields(Matrix)}"
            "}}"
        )

        async with self.client as session:
            result = await session.execute(  # type: ignore
                gql(query), {"lang": lang, "version": version}
            )
            return [Matrix(**data) for data in result["matrices"]]
