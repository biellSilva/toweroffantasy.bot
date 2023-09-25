import aiohttp
import json

from typing import Literal, Optional, Union, Tuple

from src.config import base_url_dict


data_base = {}
'''
exemple of `data_base` after been synced


```py
{
    'matrices': [
        {'alyss': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/matrices/alyss.json'},
        {'annabella': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/matrices/annabella.json'} ],

    'relics': [
        {'alternate-destiny': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/relics/alternate-destiny.json'},
        {'booster-shot': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/relics/booster-shot.json'} ],

    'simulacra': [
        {'alyss': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/simulacra/alyss.json'},
        {'annabella': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/simulacra/annabella.json'} ],

    'weapons': [
        {'alyss': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/weapons/alyss.json'},
        {'annabella': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/weapons/annabella.json'} ],

    'mounts' : [
        {'2613': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/mounts/2613.json'},
        {'aidan-knight': 'https://github.com/whotookzakum/toweroffantasy.info/blob/main/src/lib/data/mounts/aidan-knight.json'} ],

    'smart-servants' : [
        {'angel-of-nothingness': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/smart-servants/angel-of-nothingness.json'},
        {'angela': 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/smart-servants/angela.json'} ]
}
```
'''

async def get_ratelimit() -> dict:
    '''
    return a dictionary with the ratelimit from https://api.github.com/rate_limit
    '''
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://api.github.com/rate_limit') as res:
            x: dict = await res.json()
            return x.get('rate')
    

async def get_git_data(
        name: Optional[str] = None, 
        data_folder: Optional[Literal['simulacra', 'matrices', 'weapons', 'relics', 'smart-servants', 'mounts']] = None,
        data_type: Optional[Literal['json', 'names']] = 'json',
        sync: Optional[bool] = False
    ) -> Union[dict, list]:

    '''
    ### Loop through all git data from toweroffantasy.info

    if data_type is `'json'` returns a dictionary

    if is `'names'` returns a list with all names from this folder
    '''
    
    headers = {
        'User-Agent':'request'
    }

    if sync or len(data_base) == 0:
        if sync == True:
            data_base.clear()

        async with aiohttp.ClientSession(base_url='https://api.github.com', headers=headers) as cs:
            for folder in ['relics', 'smart-servants', 'mounts']:
                async with cs.get(f'/repos/whotookzakum/toweroffantasy.info/contents/src/lib/data/{folder}') as res:
                    if res.status == 200:
                        dict_data = json.loads(s=await res.read())
                        data_base[folder] = []
                        for data_file in dict_data:
                            if 'booster-shot' in data_file['name']:
                                data_base[folder].append({'overdrive-shot' : str(data_file['download_url'])})
                            else:
                                data_base[folder].append({str(data_file['name']).removesuffix('.json') : str(data_file['download_url'])})

                        print(f' - synced {folder} | {len(data_base[folder])} itens')

    if not sync:
        if data_type == 'json':

            async with aiohttp.ClientSession() as cs:
                for data in data_base.get(data_folder):
                    for i_name, url in data.items():
                        if name.replace(' ', '-').replace("'", '').lower() == i_name:
                            async with cs.get(url) as res:
                                if res.status == 200:
                                    return json.loads(s=await res.read())
                                else:
                                    raise aiohttp.ClientConnectionError(res.status, res.url)


                for data in data_base.get(data_folder):
                    for i_name, url in data.items():
                        if name.replace(' ', '-').replace("'", '').lower() in i_name:
                            async with cs.get(url) as res:
                                if res.status == 200:
                                    return json.loads(s=await res.read())
                                else:
                                    raise aiohttp.ClientConnectionError(res.status, res.url)
                                
            raise CouldNotFound(name=name, local=data_folder)

        

        if data_type == 'names':
            lista = []
            for data in data_base[data_folder]:
                for name_i, url in data.items():
                    if 'cobalt' not in name_i:
                        lista.append(name_i.replace('-', ' ').title())
                        continue
                    lista.append(name_i.title())

            return lista


async def get_image(name: Union[str, Tuple], data: Literal['simulacra', 'weapons', 'matrices', 'relics', 'smart-servants', 'mounts']):

    '''
    for `simulacra` and `weapons`, `name` need to be a tuple with Global Name and CN Name 

    for `matrices` and `relics`, `name` need to be `item['imgScr']`
    '''

    async with aiohttp.ClientSession() as cs:
        if data == 'simulacra':
            for image_name in name:
                if image_name.lower() == 'gnonno':
                    image_name = 'gunonno'

                async with cs.get(f'{base_url_dict[f"{data}_image"]}/{image_name}.webp') as res:
                    if res.status == 200:
                        return res.url
                    
                async with cs.get(f'{base_url_dict[f"{data}_image"]}/{image_name.lower()}.webp') as res:
                    if res.status == 200:
                        return res.url
                    
        elif data == 'relics':
            async with cs.get(f'{base_url_dict["relics_bigger"]}/{name}.webp') as res:
                if res.status == 200:
                    return res.url
            
            async with cs.get(f'{base_url_dict["relics_lower"]}/{name}.webp') as res:
                if res.status == 200:
                    return res.url
    
        else:
            async with cs.get(f'{base_url_dict[f"{data}_image"]}/{name}.webp') as res:
                if res.status == 200:
                    return res.url
                
    return None





class CouldNotFound(Exception):
    '''
    Custom exception called when it coundn't find the requested item in the database

    takes and returns `name` and `local`
    '''

    def __init__(self, name: str, local: str):
        self.name = name
        self.local = local
        super().__init__(self.name, self.local)

