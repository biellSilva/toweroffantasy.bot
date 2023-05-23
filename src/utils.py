import discord

from src.config import db_client, simulacra_collection, emojis


def ping_db():
    try:
        db_client.glob.command('ping')
        return 'Connected'
    except Exception:
        return False
    

async def home_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = em.title.replace('[CN]', '')

    simulacra = simulacra_collection.find_one({'name': name})
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

    url_name = name.replace(' ', '-').lower()
    em.url = f'https://toweroffantasy.info/simulacra/{url_name}'

    em.clear_fields()
    for region, voiceActor in simulacra['voiceActors'].items():
        em.add_field(name=region.upper(), value=voiceActor, inline=True)

    return em    
    

async def trait_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = em.title.replace('[CN]', '')

    simulacra = simulacra_collection.find_one({'name': name})

    em.clear_fields()
    em.description = 'Traits:'

    for trait in simulacra['traits']:
        em.add_field(name=f'Affinity {trait["affinity"]}', value=trait['description'], inline=False)

    return em


async def weapon_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = em.title.replace('[CN]', '')

    simulacra = simulacra_collection.find_one({'name': name})
    weapon = simulacra['weapon']

    em.clear_fields()
    em.description = f'''
                      Name: {weapon['name']} 
                      Shatter: *{weapon['shatter']['value']} **{weapon['shatter']['tier']}***
                      Charge: *{weapon['charge']['value']} **{weapon['charge']['tier']}**
                      '''
    # {bot.get_emoji(emojis[weapon['element']])} {bot.get_emoji(emojis[weapon['type']])}
    return em