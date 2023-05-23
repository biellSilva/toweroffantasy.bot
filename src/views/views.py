import discord

from src.utils import trait_button_func, home_button_func, weapon_button_func


class MainView(discord.ui.View):

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''

        em = await weapon_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView())


    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''trait Button'''

        await interaction.response.defer()
        em = await trait_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView())




class TraitView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())




class WeaponView(discord.ui.View):

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView())