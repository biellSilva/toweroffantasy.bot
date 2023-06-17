import discord

from src.utils import get_git_data


class ServantView(discord.ui.View):


    @discord.ui.button(custom_id='servant_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def servant_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '').removesuffix(' ')
        
        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')

        em.clear_fields()

        for star, advanc in enumerate(servant['advancements']):
            em.add_field(name=f'{star+1} ★', value=f'{advanc}')

        await interaction.message.edit(embeds=[em], attachments=[], view=ServantView())


    @discord.ui.button(custom_id='servant_abilit', label='Abilities', style=discord.ButtonStyle.grey)
    async def servant_abilit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        name = em.title.replace("'", '').replace('[CN]', '').removesuffix(' ')

        servant: dict = await get_git_data(name=name, data_folder='smart-servants', data_type='json')

        em.clear_fields()

        for abilit in servant['abilities']:
            em.add_field(name=abilit['name'], value=abilit['effect'])

        await interaction.message.edit(embeds=[em], attachments=[], view=ServantView())
    