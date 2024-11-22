from discord import Locale

from src.api._base import ApiBaseService
from src.models.matrices import MatrixSuit
from src.types import LangsEnum
from src.utils import convert_locale


class MatricesService(ApiBaseService[MatrixSuit]):
    _PATH = "/matrices"

    async def _update_cache(self, lang: LangsEnum) -> None:
        async with self._get_client() as client:
            async with client.get(self._PATH, params={"lang": lang}) as response:
                data = [MatrixSuit(**matrix) for matrix in await response.json()]
                self._cache[lang] = {matrix.id: matrix for matrix in data}

    async def get_matrix(self, lang: Locale, matrix_id: str) -> MatrixSuit:
        async with self._get_client() as client:
            async with client.get(
                f"{self._PATH}/{matrix_id}", params={"lang": convert_locale(lang)}
            ) as response:
                return MatrixSuit(**await response.json())

    async def get_matrices(self, lang: Locale) -> list[MatrixSuit]:
        async with self._get_client() as client:
            async with client.get(
                self._PATH, params={"lang": convert_locale(lang)}
            ) as response:
                return [MatrixSuit(**matrix) for matrix in await response.json()]
