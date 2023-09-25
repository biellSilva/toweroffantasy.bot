import aiohttp
import json


async def get_ratelimit() -> dict[str, ]:
    '''
    return a dictionary with the ratelimit from https://api.github.com/rate_limit
    '''
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.github.com/rate_limit') as res:
            x: dict = await res.json()
            return x.get('rate')