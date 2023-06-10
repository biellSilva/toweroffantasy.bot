import discord

from src.utils import get_data


class RelicView(discord.ui.View):

    @discord.ui.button(custom_id='relic_home', label='Home', style=discord.ButtonStyle.grey)
    async def relic_home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '').split()[:-1]

        relic = await get_data(name=''.join(name), data='relics', src='json')

        em.description = relic['description']

        await interaction.message.edit(embeds=[em], attachments=[], view=RelicView())

    @discord.ui.button(custom_id='relic_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def relic_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '').split()[:-1]

        relic = await get_data(name=''.join(name), data='relics', src='json')

        em.description = ''.join(relic['advancements'])

        await interaction.message.edit(embeds=[em], attachments=[], view=RelicView())
    