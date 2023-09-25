

from src.errorHandler.customErrors import DataNotFound
from src.config import SIMULACRA_DATA, MATRICES_DATA

from src.models.simulacra import Simulacra, Matrice



async def get_simulacra(name: str) -> Simulacra:
    data = SIMULACRA_DATA.get(name.lower(), None)
    if data:
        return data
    raise DataNotFound(name=name)

async def get_matrice(name: str) -> Matrice:
    data = MATRICES_DATA.get(name.lower(), None)
    if data:
        return data
    raise DataNotFound(name=name)
