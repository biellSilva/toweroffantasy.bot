import discord

from src.config import simulacras_names, matrices_names, relics_names


class NamesView(discord.ui.View):

    @discord.ui.button(custom_id='simulacras_help', label='Simulacras', style=discord.ButtonStyle.grey)
    async def simulacras_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        em = interaction.message.embeds[0]

        em.title = 'Simulacras'
        em.description = ', '.join(simulacras_names)

        await interaction.message.edit(embeds=[em], attachments=[], view=NamesView())

    @discord.ui.button(custom_id='matrices_help', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrices_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]

        em.title = 'Matrices'
        em.description = ', '.join(matrices_names)

        await interaction.message.edit(embeds=[em], attachments=[], view=NamesView())
    
    @discord.ui.button(custom_id='relics_help', label='Relics', style=discord.ButtonStyle.grey)
    async def relics_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]

        em.title = 'Relics'
        em.description = ', '.join(relics_names)

        await interaction.message.edit(embeds=[em], attachments=[], view=NamesView())