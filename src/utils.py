import aiohttp
import json

from typing import Literal

from src.config import matrices_names, base_url_dict, relics_names


def check_name(name: str):
    for correct_name in matrices_names:
        if name.split(' ')[0].lower() in correct_name.lower():
            return correct_name.replace(' ', '-').lower()
    
    raise NameError(name)

def check_relic(name: str):
    if 'overdrive' in name.lower():
            name = 'booster shot'
 
    for correct_name in relics_names:
        if name.lower() in correct_name.lower():
            return correct_name.replace(' ', '-').lower()
    
    raise NameError(name)


async def get_data(name, data: Literal['simulacra', 'weapons', 'matrices', 'relics'], src: Literal['json', 'image']):

    '''
    for `simulacra` and `weapons` if `src == 'image'`, `name` need to be a tuple with Global Name and CN Name 

    for `matrices` and `relics` if `src == 'image'`, `name` need to be `item['imgScr']`
    '''

    async with aiohttp.ClientSession() as cs:
        if src == 'json':
            if data in ('simulacra', 'weapons', 'matrices'):
                name = check_name(name)
            else:
                name = check_relic(name)

            if name:
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