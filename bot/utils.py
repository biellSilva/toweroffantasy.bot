import aiohttp
from typing import Any


async def get_ratelimit() -> dict[str, Any]:
    '''
    return a dictionary with the ratelimit from https://api.github.com/rate_limit
    '''
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.github.com/rate_limit') as res:
            x: dict[str, Any] = await res.json()
            return x.get('rate', {'error': '"rate" was not found'})