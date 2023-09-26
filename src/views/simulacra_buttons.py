import discord

from src.config import base_url_dict

from src.models.simulacra import Simulacra


async def home_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()

    em.description = ''

    if simulacra.cnName and simulacra.cnName not in ('', ' ', '???'):
        em.description += f"**CN Name:** {simulacra.cnName.capitalize()}\n"
        
    if simulacra.gender and simulacra.gender not in ('', ' ', '???'):
        em.description += f"**Gender:** {simulacra.gender}\n"

    if simulacra.height and simulacra.height not in ('', ' ', '???'):
        em.description += f"**Height:** {simulacra.height}\n"

    if simulacra.birthday and simulacra.birthday not in ('', ' ', '???'):
        em.description += f"**Birthday:** {simulacra.birthday}\n"

    if simulacra.birthplace and simulacra.birthplace not in ('', ' ', '???'):
        em.description += f"**Birthplace:** {simulacra.birthplace}\n"

    if simulacra.horoscope and simulacra.horoscope not in ('', ' ', '???'):
        em.description += f"**Horoscope:** {simulacra.horoscope}"
    
    em.set_thumbnail(url=await simulacra.simulacra_image())

    for region, voiceActor in simulacra.voiceActors.model_dump().items():
        if voiceActor == '' or voiceActor == None:
            continue
        em.add_field(name=region.upper(), value=voiceActor, inline=True)

    return em    
    

async def trait_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.description = None
    em.clear_fields()

    for trait in simulacra.traits:
        em.add_field(name=f'Affinity {trait.affinity}', value=trait.description, inline=False)

    return em


async def matrice_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = None

    em.set_thumbnail(url=simulacra.matrice.imgSrc)

    for set_ in simulacra.matrice.sets:
        em.add_field(name=f'{set_.pieces}x Pieces', value=set_.description, inline=False)

    return em


async def weapon_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()

    em.set_thumbnail(url=simulacra.weapon.imgSrc)

    em.description = (f"**{simulacra.weapon.name}** {simulacra.weapon.element_emoji} {simulacra.weapon.type_emoji}\n"
                      f"Shatter: *{simulacra.weapon.shatter.value} **{simulacra.weapon.shatter.tier}***\n"
                      f"Charge: *{simulacra.weapon.charge.value} **{simulacra.weapon.charge.tier}***\n"
                      f"Base stats: *{' - '.join(simulacra.weapon.baseStats).title()}*\n")
    
    if simulacra.weapon.analysisVideoSrc:
        em.description += f'\n[Analysis Video]({simulacra.weapon.analysisVideoSrc})'
    
    if simulacra.weapon.abilitiesVideoSrc:
        em.description += f'\n[Abilities Video]({simulacra.weapon.abilitiesVideoSrc})'

    if simulacra.weapon.weaponEffects:
        for effect in simulacra.weapon.weaponEffects:
            em.add_field(name=effect.title, value=effect.description, inline=False)

    return em


async def advanc_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]

    em.clear_fields()
    em.description = None

    for ind, advanc in enumerate(simulacra.weapon.advancements, start=1):
        em.add_field(name=f'{ind} ★', value=advanc, inline=False)
    
    return em



async def meta_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]

    em.clear_fields()
    em.description = None
    
    if not len(simulacra.weapon.recommendedPairings) == 0:
        em.add_field(name='Recommended Pairings', 
                        value='\n'.join(f'**[{name.capitalize()}]({base_url_dict["simulacra_home"]}{name.replace(" ","-").lower()})**' 
                                        for name in simulacra.weapon.recommendedPairings), 
                        inline=False)

    if not len(simulacra.weapon.recommendedMatrices) == 0:
        em.add_field(name='Recommended Matrices', 
                        value='\n'.join(f'**[{matrix.pieces}x {matrix.name.capitalize()}]({base_url_dict["simulacra_home"]}{matrix.name.replace(" ","-").lower()})**' 
                                        for matrix in simulacra.weapon.recommendedMatrices), 
                        inline=False)

    return em


async def abilities_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = ''

    for abilitie in simulacra.weapon.abilities:
        if 'skill' in abilitie.type:
            em.description += f"\n\n**{abilitie.name.title()}** *[ {abilitie.type.capitalize()} ]*\n{abilitie.description}"
            
    return em


async def discharge_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = ''

    for abilitie in simulacra.weapon.abilities:
        if 'discharge' in abilitie.type:
            em.description += f"\n\n**{abilitie.name.title()}** *[ {abilitie.type.capitalize()} ]*\n{abilitie.description}"
            
    return em


async def weapon_normal_attack_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = ''

    for abilitie in simulacra.weapon.abilities:
        if 'normal' in abilitie.type:
            if abilitie.input and 'Jump' not in abilitie.input:
                input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input)} ]*"

                em.description += (f"\n\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n")
                
                if abilitie.breakdown:
                    em.description+= '**Breakdown:**\n'
                    em.description+= '\n'.join(abilitie.breakdown)

            elif not abilitie.input:
                em.description += (f"\n\n**{abilitie.name}** \n"
                                    f"{abilitie.description}\n")
                    
                if 'breakdown' in abilitie:
                    em.description+= '**Breakdown:**\n'
                    em.description+= '\n'.join(abilitie.breakdown)

    return em


async def weapon_jump_attack_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = ''

    for abilitie in simulacra.weapon.abilities:
        if 'normal' in abilitie.type and abilitie.input and 'Jump' in abilitie.input:
            input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input).title()} ]*"

            em.description += (f"\n\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n")
            
            if abilitie.breakdown:
                em.description+= '**Breakdown:**\n'
                em.description+= '\n'.join(abilitie.breakdown)
    return em


async def weapon_dodge_attack_button_func(interaction: discord.Interaction, simulacra: Simulacra):
    em = interaction.message.embeds[0]
    em.clear_fields()
    em.description = ''

    for abilitie in simulacra.weapon.abilities:
        if 'dodge' in abilitie.type:

            input_ = '' if not abilitie.input or len(abilitie.input) == 0 else f"*[ {' - '.join(abilitie.input).title()} ]*"

            em.description += (f"\n\n**{abilitie.name.title()}** {input_}\n{abilitie.description}\n")
            
            if abilitie.breakdown:
                em.description+= '**Breakdown:**\n'
                em.description+= '\n'.join(abilitie.breakdown)

    return em