import aiohttp
import json

from src.models.matrices import Matrice
from src.models.simulacra import Simulacra
from src.config import SIMULACRA_DATA, MATRICES_DATA


async def update_cache():
    async with aiohttp.ClientSession() as cs:
        for folder in ['simulacra', 'matrices']:
            async with cs.get(f'https://api.github.com/repos/whotookzakum/toweroffantasy.info/contents/src/lib/data/{folder}', headers={'User-Agent':'request'}) as res:
                if res.status == 200:
                    dict_data = json.loads(s=await res.read())
                    print(f'syncing {folder}')

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
                                    matrice_dict = json.loads(s=await res.read())

                            data = Matrice(**matrice_dict)
                            MATRICES_DATA.update({data.name.lower(): data})
                        
    print(f'simulacras - {len(SIMULACRA_DATA)}\n'
            f'matrices - {len(MATRICES_DATA)}')