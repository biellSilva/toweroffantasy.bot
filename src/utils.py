import aiohttp
import json

from typing import Literal

from src.config import names, base_url_dict


def check_name(name: str):
    for _ in names:
        if name.split(' ')[0].lower() in _.lower():
            return str(_) 

    return None


async def get_data(name, data: Literal['simulacra', 'weapons', 'matrices'], src: Literal['json', 'image']):

    '''
    for `simulacra` and `weapons` if `src == 'image'`, `name` need to be a tuple with Global Name and CN Name 

    for `matrices` if `src == 'image'`, `name` need to be `matrice['imgScr']`
    '''

    async with aiohttp.ClientSession() as cs:
        if src == 'json':
            name = check_name(name)

            if name: 
                name = name.replace(' ', '-').lower()

                async with cs.get(f'{base_url_dict["data_json"]}/{data}/{name}.json') as res:
                    if res.status == 200:
                        return json.loads(s=await res.read())
                
        if src == 'image':
            if data == 'simulacra':
                for image_name in name:
                    if image_name.lower() == 'gnonno':
                        image_name = 'gunonno'

                    async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{image_name}.webp') as res:
                        if res.status == 200:
                            return res.url
                        
                    async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{image_name.lower()}.webp') as res:
                        if res.status == 200:
                            return res.url
            else:
                async with cs.get(f'{base_url_dict[f"{data}_{src}"]}/{name}.webp') as res:
                    if res.status == 200:
                        return res.url
                
    return None