
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot.infra.entitys import *


SIMULACRA_DATA: dict[str, 'Simulacra'] = {}
MATRICES_DATA: dict[str, 'Matrice'] = {}
RELICS_DATA: dict[str, 'Relic'] = {}
MOUNTS_DATA: dict[str, 'Mount'] = {}
SERVANTS_DATA: dict[str, 'SmartServant'] = {}

## GUILD
BOT_GUILD = 1000974290801410138
FEEDBACK_CATEGORY = 1117793661141393508


##  EMOJIS
EMOJIS = {
    'dps' : '<:dps:1097910880756310176>',
    'defense' : '<:def:1097910876255826050>',
    'support' : '<:sup:1097910879187632308>',

    'attack': '<:icon_atk:1170591016269643857>',
    'crit': '<:icon_crit:1170591046049214484>',
    'resistance': '<:icon_resist:1170591062889332907>',
    'health': '<:icon_hp:1170591060330811434>',
    
    'flame': '<:flame:1097910889920864336>',
    'ice' : '<:frost:1097910888280895730>',
    'volt' : '<:volt:1097910883155456044>',
    'physical' : '<:physic:1097910885529432164>',
    'altered': '<:altered:1097910892504567829>',
    'physical-flame': '<:phisycal_flame:1145748266055643216>'
}



## URLS
base_url_dict = {
    'simulacra_home': 'https://toweroffantasy.info/simulacra/',
    'matrice_home' : 'https://toweroffantasy.info/matrices/',
    'relics_home' : 'https://toweroffantasy.info/relics/',
    
    'simulacra_image' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/huanxing/lihui',
    'weapons_image' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/weapon/Icon',
    'matrices_image' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/Icon/yizhi/256',
    'relics_bigger' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Artifact/itemicon',
    'relics_lower' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Artifact/icon',
    'smart-servants_image' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/PetFight/icon',
    'mounts_image' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/static/images/UI/Mount',

    'data_json' : 'https://raw.githubusercontent.com/whotookzakum/toweroffantasy.info/main/src/lib/data/',
}