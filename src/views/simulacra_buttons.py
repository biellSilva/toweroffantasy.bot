import discord

from src.config import emojis_1, base_url_dict
from src.utils import get_git_data, get_image


async def home_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    simulacra: dict = await get_git_data(name=name, data_folder='simulacra', data_type='json')
    thumb_url = await get_image(name=(simulacra['name'], simulacra['cnName']), data='simulacra')

    skin_url = f"[Skin Preview]({simulacra['skinsPreviewUrl']})" if 'skinsPreviewUrl' in simulacra else ''
    
    em.description=(f"CN Name: {simulacra['cnName'].capitalize()}\n"
                    f"Gender: {simulacra['gender']}\n"
                    f"Height: {simulacra['height']}\n"
                    f"Birthday: {simulacra['birthday']}\n"
                    f"Birthplace: {simulacra['birthplace']}\n"
                    f"Horoscope: {simulacra['horoscope']}\n\n"

                    f"{skin_url}" )
    
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
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    simulacra: dict = await get_git_data(name=name, data_folder='simulacra', data_type='json')

    em.description = ''
    em.clear_fields()
    for trait in simulacra['traits']:
        em.add_field(name=f'Affinity {trait["affinity"]}', value=trait['description'], inline=False)

    return em


async def matrice_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    matrice = await get_git_data(name=name, data_folder='matrices', data_type='json')
    thumb_url = await get_image(name=matrice['imgSrc'], data='matrices')

    em.clear_fields()

    for set_ in matrice['sets']:
        em.add_field(name=f'{set_["pieces"]}x', value=set_["description"], inline=False)

    if thumb_url:
        em.set_thumbnail(url=thumb_url)
    
    return em


async def weapon_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')
    thumb_url = await get_image(name=weapon['imgSrc'], data='weapons')

    analysisVideo = f"[Analysis Video]({weapon['analysisVideoSrc']})" if 'analysisVideoSrc' in weapon else ''
    abilitiesVideo = f"[Abilities Video]({weapon['abilitiesVideoSrc']})" if 'abilitiesVideoSrc' in weapon else ''

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
        for effect in weapon['weaponEffects']:
            em.add_field(name=effect['title'], value=effect['description'], inline=False)

    return em


async def advanc_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    for ind, advanc in enumerate(weapon['advancements']):
        em.add_field(name=f'{ind+1} ★', value=advanc, inline=False)
    
    return em



async def meta_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    desc = ''
    for name in weapon['recommendedPairings']:
        name : str
        url_name = name.replace(' ','-').lower()
        desc += f'\n**[{name.capitalize()}]({base_url_dict["simulacra_home"]}{url_name})**'
    
    if desc != '':
        em.add_field(name='Recommended Pairings', value=desc, inline=False)

    desc = ''
    for matrix in weapon['recommendedMatrices']:
        matrix: dict
        url_name = matrix['name'].replace(' ', '-').lower()
        desc += f'\n{matrix["pieces"]}x **[{matrix["name"]}]({base_url_dict["matrice_home"]}{url_name})**'

    if desc != '':
        em.add_field(name='Recommended Matrices', value=desc, inline=False)

    return em


async def abilities_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'skill' in abilitie['type']:
            em.description += (f"\n\n**{abilitie['name'].title()}** *[ {abilitie['type'].capitalize()} ]*\n"
                               f"{abilitie['description']}")
            
    return em


async def discharge_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'discharge' in abilitie['type']:
            em.description += (f"\n\n**{abilitie['name'].title()}** *[ {abilitie['type'].capitalize()} ]*\n"
                               f"{abilitie['description']}")
            
    return em


async def weapon_normal_attack_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'normal' in abilitie['type']:
            if 'input' in abilitie:
                if 'Jump' not in abilitie['input']:
                    input_ = '' if 'input' not in abilitie or len(abilitie['input']) == 0 else f"*[ {' - '.join(abilitie['input'])} ]*"

                    em.description += (f"\n\n**{abilitie['name'].title()}** {input_}\n"
                                    f"{abilitie['description']}\n")
                    
                    if 'breakdown' in abilitie:
                        em.description+= '**Breakdown:**\n'
                        em.description+= '\n'.join(abilitie['breakdown'])
            else:
                em.description += (f"\n\n**{abilitie['name']}** \n"
                                    f"{abilitie['description']}\n")
                    
                if 'breakdown' in abilitie:
                    em.description+= '**Breakdown:**\n'
                    em.description+= '\n'.join(abilitie['breakdown'])

    return em


async def weapon_jump_attack_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'normal' in abilitie['type']:
            if 'input' in abilitie:
                if 'Jump' in abilitie['input']:

                    input_ = '' if 'input' not in abilitie or len(abilitie['input']) == 0 else f"*[ {' - '.join(abilitie['input']).title()} ]*"

                    em.description += (f"\n\n**{abilitie['name'].title()}** {input_}\n"
                                    f"{abilitie['description']}\n")
                    
                    if 'breakdown' in abilitie:
                        em.description+= '**Breakdown:**\n'
                        em.description+= '\n'.join(abilitie['breakdown'])
    return em


async def weapon_dodge_attack_button_func(interaction: discord.Interaction):
    em = interaction.message.embeds[0]
    name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

    weapon: dict = await get_git_data(name=name, data_folder='weapons', data_type='json')

    em.clear_fields()

    em.description = ''

    for abilitie in weapon['abilities']:
        if 'dodge' in abilitie['type']:

            input_ = '' if 'input' not in abilitie or len(abilitie['input']) == 0 else f"*[ {' - '.join(abilitie['input']).title()} ]*"

            em.description += (f"\n\n**{abilitie['name'].title()}** {input_}\n"
                            f"{abilitie['description']}\n")
            
            if 'breakdown' in abilitie:
                em.description+= '**Breakdown:**\n'
                em.description+= '\n'.join(abilitie['breakdown'])

    return em