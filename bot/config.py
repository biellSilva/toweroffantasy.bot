
from discord.app_commands import Choice


## GUILD
BOT_GUILD = 1000974290801410138
FEEDBACK_CATEGORY = 1117793661141393508


##  EMOJIS
EMOJIS = {
    'DPS' : '<:dps:1097910880756310176>',
    'Tank' : '<:def:1097910876255826050>',
    'SUP' : '<:sup:1097910879187632308>',

    'attack': '<:icon_atk:1170591016269643857>',
    'crit': '<:icon_crit:1170591046049214484>',
    'resistance': '<:icon_resist:1170591062889332907>',
    'health': '<:icon_hp:1170591060330811434>',
    
    'Flame': '<:flame:1097910889920864336>',
    'Ice' : '<:frost:1097910888280895730>',
    'Volt' : '<:volt:1097910883155456044>',
    'Physics' : '<:physic:1097910885529432164>',
    'Superpower': '<:altered:1097910892504567829>',
    'PhysicsFlame': '<:phisycal_flame:1145748266055643216>'
}
STAR_EMOJI = '★'

API_LANGS = ['de', 'en', 'es', 'fr', 'id', 'ja', 'pt', 'ru', 'th', 'zh-cn', 'zh-hans-sg']
API_LANGS_CHOICE: list[Choice[str]] = [Choice(name=i, value=i) for i in API_LANGS]