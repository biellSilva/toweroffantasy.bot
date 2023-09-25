import discord

from src.models import Relic


class RelicView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, relic: Relic):
        self.relic = relic
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='relic_home', label='Home', style=discord.ButtonStyle.grey)
    async def relic_home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        em = interaction.message.embeds[0]

        em.description = self.relic.description

        await interaction.message.edit(embed=em)

    @discord.ui.button(custom_id='relic_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def relic_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        em.description = ''

        for star, advanc in enumerate(self.relic.advancements):
            em.description += (f'**{star+1} ★**\n'
                               f'{advanc}\n\n')

        await interaction.message.edit(embed=em)
    