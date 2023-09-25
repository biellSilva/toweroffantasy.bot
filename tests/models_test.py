import requests
from src.models import Simulacra, Matrice, Relic, Mount, SmartServant
from pprint import pprint
from asyncio import run


async def foo(data: Simulacra):
    print(await data.simulacra_image())

url = ['https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/simulacra/alyss.json', 
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/simulacra/mimi.json',
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/weapons/mimi.json',
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/matrices/mimi.json',
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/relics/colossus-arm.json',
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/mounts/floating-bubble-water.json',
       'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/smart-servants/angel-of-nothingness.json']

# req = requests.get(url=url[1])
# req_w = requests.get(url=url[2])
# req_m = requests.get(url=url[3])
# if req.status_code == 200 and req_w.status_code == 200 and req_m.status_code == 200:

#     data = Simulacra(**req.json(), weapon=req_w.json(), matrice=req_m.json())

#     pprint(data.model_dump(), sort_dicts=False)
#     run(foo(data=data))

req = requests.get(url=url[6])
if req.status_code == 200:
    data = SmartServant(**req.json())

    pprint(data.model_dump(), sort_dicts=False)
