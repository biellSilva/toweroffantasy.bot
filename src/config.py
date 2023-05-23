from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import get_key, find_dotenv

##  MONGO DB CONNECTION
user = get_key(dotenv_path=find_dotenv(), key_to_get='db_user')
pw = get_key(dotenv_path=find_dotenv(), key_to_get='db_pass')
uri = get_key(dotenv_path=find_dotenv(), key_to_get='db_uri')

db_client = MongoClient(uri.replace('<username>', user).replace('<password>', pw), server_api=ServerApi('1'))

glob = db_client.glob # global database
matrice_collection = glob.matrice
simulacra_collection = glob.simulacra


##  COLORS
no_bar = 0x2b2d31


##  EMOJIS
emojis = {
    'dps' : 1097910880756310176,
    'defense' : 1097910876255826050,
    'support' : 1097910879187632308,
    
    'flame': 1097910889920864336,
    'ice' : 1097910888280895730,
    'volt' : 1097910883155456044,
    'physical' : 1097910885529432164,
    'altered': 1097910892504567829
}

emojis_1 = {
    'dps' : '<:dps:1097910880756310176>',
    'defense' : '<:def:1097910876255826050>',
    'support' : '<:sup:1097910879187632308>',
    
    'flame': '<:flame:1097910889920864336>',
    'ice' : '<:frost:1097910888280895730>',
    'volt' : '<:volt:1097910883155456044>',
    'physical' : '<:physic:1097910885529432164>',
    'altered': '<:altered:1097910892504567829>'
}


## NAMES
names = ['Alyss', 'Annabella', 'Bai Ling', 'Baiyuekui', 'Claudia', 'Cobalt-B', 'Cocoritter', 'Crow', 'Echo', 
'Ene', 'Fenrir', 'Fiona', 'Frigg', 'Garnett', 'Gnonno', 'Hilda', 'Huma', 'Icarus', 'KING', 'Lan', 'Lin', 
'Lyra', 'Marc', 'Meryl', 'Nemesis', 'Pepper', 'Rubilia', 'Ruby', 'Saki Fuwa', 'Samir', 'Shiro', 
'Tian Lang', 'Tsubasa', 'Umi', 'Yulan', 'Zero', 'Apophis', 'Barbarossa', 'Frost Bot', 'Functional Dash',
'Haboela', 'Obstacle Removal', 'Plunder', 'Robarg', 'Scylla', 'Self Explosive', 'Sobek', 'Standard Operation',
'Wandering Aberrant', 'Wind Blade']