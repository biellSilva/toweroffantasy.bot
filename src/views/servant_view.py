import discord

from src.models import SmartServant


class ServantView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, servant: SmartServant):
        self.servant = servant
        super().__init__(timeout=timeout)


    @discord.ui.button(custom_id='servant_advanc', label='Advancements', style=discord.ButtonStyle.grey)
    async def servant_advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        em.clear_fields()

        for star, advanc in enumerate(self.servant.advancements):
            em.add_field(name=f'{star+1} ★', value=f'{advanc}', inline=False)

        await interaction.message.edit(embed=em)


    @discord.ui.button(custom_id='servant_abilit', label='Abilities', style=discord.ButtonStyle.grey)
    async def servant_abilit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        em = interaction.message.embeds[0]
        em.clear_fields()

        for abilit in self.servant.abilities:
            em.add_field(name=abilit.name, value=abilit.effect, inline=False)

        await interaction.message.edit(embed=em)
    