import aiohttp
import json

from typing import Literal

from src.models import *
from src.config import SIMULACRA_DATA, MATRICES_DATA, RELICS_DATA, MOUNTS_DATA, SERVANTS_DATA 


async def update_cache():
    async with aiohttp.ClientSession() as cs:
        for folder in ['simulacra', 'matrices', 'relics', 'mounts', 'smart-servants']:
            async with cs.get(f'https://api.github.com/repos/whotookzakum/toweroffantasy.info/contents/src/lib/data/{folder}', headers={'User-Agent':'request'}) as res:
                if res.status == 200:
                    dict_data = json.loads(s=await res.read())
                    print(f'- Syncing {folder}')

                    for data_file in dict_data:
                        url: str = data_file['download_url']
                    
                        if folder == 'simulacra':
                            simulacra_dict = None
                            weapon_dict = None
                            matrice_dict = None

                            async with cs.get(url=url) as res:
                                if res.status == 200:
                                    simulacra_dict = json.loads(s=await res.read())
                            
                            async with cs.get(url=url.replace('simulacra', 'weapons')) as res:
                                if res.status == 200:
                                    weapon_dict = json.loads(s=await res.read())

                            async with cs.get(url=url.replace('simulacra', 'matrices')) as res:
                                if res.status == 200:
                                    matrice_dict = json.loads(s=await res.read())

                            data = Simulacra(**simulacra_dict, weapon=weapon_dict, matrice=matrice_dict)
                            SIMULACRA_DATA.update({data.name.lower(): data})


                        elif folder == 'matrices':
                            matrice_dict = None

                            async with cs.get(url=url) as res:
                                if res.status == 200:
                                    data = Matrice(**json.loads(s=await res.read()))
                                    MATRICES_DATA.update({data.name.lower(): data})
                        
                        elif folder == 'relics':
                            async with cs.get(url=url) as res:
                                if res.status == 200:
                                    data = Relic(**json.loads(s=await res.read()))
                                    RELICS_DATA.update({data.name.lower(): data})
                        
                        elif folder == 'mounts':
                            async with cs.get(url=url) as res:
                                if res.status == 200:
                                    data = Mount(**json.loads(s=await res.read()))
                                    MOUNTS_DATA.update({data.name.lower(): data})
                        
                        elif folder == 'smart-servants':
                            async with cs.get(url=url) as res:
                                if res.status == 200:
                                    data = SmartServant(**json.loads(s=await res.read()))
                                    SERVANTS_DATA.update({data.name.lower(): data})
                    
                    print(f'- Synced {folder} | {len(dict_data)}')
                        