import discord
import aiohttp

from typing import Literal

from src.config import db_client, simulacra_collection, emojis_1, names, base_url_dict


def ping_db():
    try:
        db_client.glob.command('ping')
        return 'Connected'
    except Exception:
        return False


def check_name(name: str):
    for _ in names:
        if name.split(' ')[0].lower() in _.lower():
            return _ 
    return False


async def check_url(src: Literal['simulacra', 'weapon', 'matrice'], names):
    async with aiohttp.ClientSession() as cs:
        base_url = base_url_dict[src]

        if src == 'weapon':
            async with cs.get(f'{base_url}/{names}.webp') as res:
                if res.status == 200:
                    return res.url
                
        if src == 'simulacra':
            for name in names:
                if name.lower() == 'gnonno':
                    name = 'gunonno'
                async with cs.get(f'{base_url}/{name}.webp') as res:
                    if res.status == 200:
                        return res.url
                        
                async with cs.get(f'{base_url}/{name.lower()}.webp') as res:
                    if res.status == 200:
                        return res.url
        
        if src == 'matrice':
            name = names
            async with cs.get(f'{base_url[1]}/{name}.webp') as res:
                if res.status == 200:
                    return res.url
                
            name = names.replace('256', '512')
            async with cs.get(f'{base_url[0]}/{name}.webp') as res:
                if res.status == 200:
                    return res.url
    
    return False



async def home_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    skin_url = f"[Skins Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''
    
    em.description=(f"CN Name: {simulacra['cnName'].capitalize()}\n\n"

                    f"Gender: {simulacra['gender']}\n"
                    f"Height: {simulacra['height']}\n"
                    f"Birthday: {simulacra['birthday']}\n"
                    f"Birthplace: {simulacra['birthplace']}\n"
                    f"Horoscope: {simulacra['horoscope']}\n\n"

                    f"{skin_url}" )
    
    thumb_url = await check_url(src='simulacra', names=(simulacra['name'], simulacra['cnName']))
    if thumb_url:
        em.set_thumbnail(url=thumb_url)

    em.clear_fields()

    for region, voiceActor in simulacra['voiceActors'].items():
        if voiceActor == '':
            continue
        em.add_field(name=region.upper(), value=voiceActor, inline=True)

    return em    
    

async def trait_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})

    em.description = ''
    em.clear_fields()
    for trait in simulacra['traits']:
        em.add_field(name=f'Affinity {trait["affinity"]}', value=trait['description'], inline=False)

    return em


async def weapon_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    analysisVideo = f"[Analysis Video]({weapon['analysisVideoSrc']})" if 'analysisVideoSrc' in weapon else ''
    abilitiesVideo = f"[Abilities Video]({weapon['abilitiesVideoSrc']})" if 'abilitiesVideoSrc' in weapon else ''

    thumb_url = await check_url(src='weapon', names=weapon['imgSrc'])
    if thumb_url:
        em.set_thumbnail(url=thumb_url)

    em.clear_fields()
    em.description = (
                      f"**{weapon['name']}** {emojis_1[weapon['element']]} {emojis_1[weapon['type']]}\n"
                      f"Shatter: *{weapon['shatter']['value']} **{weapon['shatter']['tier']}***\n"
                      f"Charge: *{weapon['charge']['value']} **{weapon['charge']['tier']}***\n"
                      f"Base stats: *{' - '.join(weapon['baseStats']).title()}*\n"
                      )
    
    for i in [analysisVideo, abilitiesVideo]:
        if 'https' not in i:
            continue
        em.description += f'\n{i}'
    
    if 'weaponEffects' in weapon:
        for i in weapon['weaponEffects']:
            em.add_field(name=i['title'], value=i['description'], inline=False)

    return em


async def advanc_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    em.clear_fields()

    for ind, advanc in enumerate(weapon['advancements']):
        em.add_field(name=f'{ind+1} 🟊', value=advanc, inline=False)
    
    return em


async def rec_matrice_button_func(interaction: discord.Interaction):

    ''' CHANGED TO META FUNCTION '''

    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    em.clear_fields()

    for i in weapon['recommendedMatrices']:
        em.add_field(name=f'{i["pieces"]}x {i["name"]}', value=i['description'], inline=False)

    return em


async def meta_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    em.clear_fields()

    desc = ''
    for name in weapon['recommendedPairings']:
        name : str
        url_name = name.replace(' ','-').lower()
        desc += f'\n**[{name.capitalize()}]({base_url_dict["simulacra_url"]}{url_name})**'
    
    if not desc.isspace():
        em.add_field(name='Recommended Pairings', value=desc, inline=False)

    desc = ''
    for matrix in weapon['recommendedMatrices']:
        matrix: dict
        url_name = matrix['name'].replace(' ', '-').lower()
        desc += f'\n{matrix["pieces"]}x **[{matrix["name"]}]({base_url_dict["matrice_url"]}{url_name})**'

    if not desc.isspace():
        em.add_field(name='Recommended Matrices', value=desc, inline=False)

    return em


async def abilities_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    em.clear_fields()

    for abilitie in weapon['abilities']:
        if abilitie['type'] in ('skill', 'discharge'):
            em.add_field(name=f"{abilitie['name'].title()} {abilitie['type'].capitalize()}", 
                         value=abilitie['description'])
            
    return em