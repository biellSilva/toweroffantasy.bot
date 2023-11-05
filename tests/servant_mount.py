from asyncio import run 
from pprint import pprint

from tof_bot.utils import get_git_data, get_ratelimit


async def rate_test():
    x = await get_ratelimit()
    pprint(x, indent=2)


async def get_mount():
    x = await get_git_data(name='chaser', data_folder='mounts', data_type='json')
    pprint(x, indent=2)

async def get_servant():
    x = await get_git_data(name='angela', data_folder='smart-servants', data_type='json')
    pprint(x, indent=2)

run(get_servant())