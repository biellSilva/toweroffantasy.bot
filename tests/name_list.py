from asyncio import run

from tof_bot.utils import get_git_data

async def test():
    x = await get_git_data(data_folder='relics', data_type='names')
    print(x)

run(test())