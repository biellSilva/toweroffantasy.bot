import discord

from src.utils import get_git_data
from src.config import emojis_1


class ServantView(discord.ui.View):

    @discord.ui.button(custom_id='servant_home', label='Home', style=discord.ButtonStyle.grey)
    async def servant_home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '')

        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')

        em.description=(f"{emojis_1[servant['type']]} {emojis_1[servant['element']]}\n"
                       f"Attack: **{servant['attack']}** \n"
                       f"Crit: **{servant['crit']}** \n\n"
                       f"{servant['description']}")

        await interaction.message.edit(embeds=[em], attachments=[], view=ServantView())


    @discord.ui.button(custom_id='servant_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def servant_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '')

        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')

        em.description = ''

        for star, advanc in enumerate(servant['advancements']):
            em.description += (f'**{star+1} ★**\n'
                               f'{advanc}\n\n')

        await interaction.message.edit(embeds=[em], attachments=[], view=ServantView())


    @discord.ui.button(custom_id='servant_abilit', label='Abilities', style=discord.ButtonStyle.grey)
    async def servant_abilit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '')

        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')

        em.description = ''

        for abilit in servant['abilities']:
            for abilit_name, effect, imgSrc in abilit:
                em.description += (f'**{abilit_name}**\n'
                                   f'{effect}\n\n')

        await interaction.message.edit(embeds=[em], attachments=[], view=ServantView())
    