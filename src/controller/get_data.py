
from typing import Literal

from src.errorHandler.customErrors import DataNotFound
from src.config import SIMULACRA_DATA, MATRICES_DATA, RELICS_DATA, MOUNTS_DATA, SERVANTS_DATA

from src.models import *



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

async def get_mount(name: str) -> Mount:
    for data in list(MOUNTS_DATA.values()):
        if name.lower() == data.name.lower() or name.replace(' ', '').lower() == data.name.replace(' ', '').lower():
            return data
    raise DataNotFound(name=name)

async def get_relic(name: str) -> Relic:
    for data in list(RELICS_DATA.values()):
        if name.lower() == data.name.lower() or name.replace(' ', '').lower() == data.name.replace(' ', '').lower():
            return data
    raise DataNotFound(name=name)

async def get_servant(name: str) -> SmartServant:
    for data in list(SERVANTS_DATA.values()):
        if name.lower() == data.name.lower() or name.replace(' ', '').lower() == data.name.replace(' ', '').lower():
            return data
    raise DataNotFound(name=name)


async def get_names(local: Literal['simulacras', 'matrices', 'relics', 'mounts', 'smart-servants']):
    if local == 'simulacras':
        return list(SIMULACRA_DATA.values())
    elif local == 'matrices':
        return list(MATRICES_DATA.values())
    elif local == 'relics':
        return list(RELICS_DATA.values())
    elif local == 'mounts':
        return list(MOUNTS_DATA.values())
    elif local == 'smart-servants':
        return list(SERVANTS_DATA.values())