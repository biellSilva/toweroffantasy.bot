import discord

from src.config import db_client, simulacra_collection, emojis_1, names


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


async def home_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    skin_url = f"[Skins Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''
    
    em.description=f"""
                    Weapon: {simulacra['weapon']['name']}
                    Rarity: {simulacra['rarity']}
                    CN Name: {simulacra['cnName'].capitalize()}

                    Gender: {simulacra['gender']}
                    Height: {simulacra['height']}
                    Birthday: {simulacra['birthday']}
                    Birthplace: {simulacra['birthplace']}
                    Horoscope: {simulacra['horoscope']}

                    {skin_url} 
                    """
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

    recommendedPairings = f"Recommended Pairings: *{' - '.join(weapon['recommendedPairings']).title()}*" if len(weapon['recommendedPairings']) != 0 else ''
    analysisVideo = f"[Analysis Video]({weapon['analysisVideoSrc']})" if 'analysisVideoSrc' in weapon else ''
    abilitiesVideo = f"[Abilities Video]({weapon['abilitiesVideoSrc']})" if 'abilitiesVideoSrc' in weapon else ''

    em.clear_fields()
    em.description = f'''
                      **{weapon['name']}** {emojis_1[weapon['element']]} {emojis_1[weapon['type']]}
                      Shatter: *{weapon['shatter']['value']} **{weapon['shatter']['tier']}***
                      Charge: *{weapon['charge']['value']} **{weapon['charge']['tier']}***
                      Base stats: *{" - ".join(weapon['baseStats']).title()}* '''
    
    if recommendedPairings:
        em.description += f'\n {recommendedPairings} \n'
    else:
        em.description += '\n'
    
    for i in [analysisVideo, abilitiesVideo]:
        if i == '':
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
    em = interaction.message.embeds[0]

    simulacra = simulacra_collection.find_one({'name': check_name(em.title)})
    weapon = simulacra['weapon']

    em.clear_fields()

    for i in weapon['recommendedMatrices']:
        em.add_field(name=f'{i["pieces"]}x {i["name"]}', value=i['description'], inline=False)

    return em