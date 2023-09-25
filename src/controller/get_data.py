
from typing import Literal

from src.errorHandler.customErrors import DataNotFound
from src.config import SIMULACRA_DATA, MATRICES_DATA

from src.models.simulacra import Simulacra, Matrice



async def get_simulacra(name: str) -> Simulacra:
    for data in list(SIMULACRA_DATA.values()):
        if (name.lower() == data.name.lower() or name.replace(' ', '').lower() == data.name.replace(' ', '').lower()
            or name.lower() == data.cnName.lower() or name.replace(' ', '').lower() == data.cnName.replace(' ', '').lower()):
            return data
    raise DataNotFound(name=name)

async def get_matrice(name: str) -> Matrice:
    for data in list(MATRICES_DATA.values()):
        if name.lower() == data.name.lower() or name.replace(' ', '').lower() == data.name.replace(' ', '').lower():
            return data
    raise DataNotFound(name=name)

async def get_names(local: Literal['simulacras', 'matrices']):
    if local == 'simulacras':
        return list(SIMULACRA_DATA.values())
    if local == 'matrices':
        return list(MATRICES_DATA.values())
