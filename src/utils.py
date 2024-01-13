import aiohttp

from typing import Any
from discord import Locale


async def get_ratelimit() -> dict[str, Any]:
    '''
    return a dictionary with the ratelimit from https://api.github.com/rate_limit
    '''
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.github.com/rate_limit') as res:
            x: dict[str, Any] = await res.json()
            return x.get('rate', {'error': '"rate" was not found'})

def convert_lang(locale: Locale) -> str:
    LANGS = {
        'en-US': 'en',
        'en-GB': 'en',
        'zh-CN': 'zh-cn', 
        'zh-TW': 'zh-hans-sg',
        'pt-BR': 'pt',
        'es-ES': 'es',
        'de': 'de',
        'ja': 'ja',
        'ru': 'ru',
        'fr': 'fr',
        'id': 'id',
        'th': 'th'
    }
    return LANGS.get(locale.value, 'en')

def convert_rarity(rarity: int) -> str:
    return {
        1: '',
        2: 'N',
        3: 'R',
        4: 'SR',
        5: 'SSR',
    }.get(rarity, '')


def convert_operations(operations: list[str]):
    counter: list[str] = []

    last_input: str | None = None
    input_counter: int = 1

    for indx, input_ in enumerate(operations, start=1):
        if last_input and input_ == last_input:
            input_counter += 1
        
        elif input_ != last_input:
            if last_input:
                if input_counter > 1:
                    counter.append(f'{last_input} {input_counter}x')
                else:
                    counter.append(last_input)
            
            last_input = input_
            input_counter = 1

        if last_input and indx == len(operations):

            if input_counter > 1:
                counter.append(f'{last_input} {input_counter}x')
            else:
                counter.append(last_input)

    return ' - '.join(counter)