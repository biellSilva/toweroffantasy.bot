import discord

from src.utils import get_git_data


class RelicView(discord.ui.View):

    @discord.ui.button(custom_id='relic_home', label='Home', style=discord.ButtonStyle.grey)
    async def relic_home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        em = interaction.message.embeds[0]
        name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

        relic: dict = await get_git_data(name=name, data_folder='relics', data_type='json')

        em.description = relic['description']

        await interaction.message.edit(embeds=[em], attachments=[], view=RelicView())

    @discord.ui.button(custom_id='relic_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def relic_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = ' '.join(em.title.replace("'", '').replace('[CN]', '').split()[:-1])

        relic: dict = await get_git_data(name=name, data_folder='relics', data_type='json')

        em.description = ''

        for star, advanc in enumerate(relic['advancements']):
            em.description += (f'**{star+1} ★**\n'
                               f'{advanc}\n\n')

        await interaction.message.edit(embeds=[em], attachments=[], view=RelicView())
    