
import discord

from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from bot.infra.entitys import Weapon


class WeaponView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, weapon: 'Weapon', owner: Union[discord.User, discord.Member]):
        self.weapon = weapon
        self.owner = owner
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label='Main', style=discord.ButtonStyle.grey)
    async def main_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_main)
    
    @discord.ui.button(label='Advancements', style=discord.ButtonStyle.grey)
    async def advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_advanc)
    
    @discord.ui.button(label='Effects', style=discord.ButtonStyle.grey)
    async def effects_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_effects)
    
    @discord.ui.button(label='Skills', style=discord.ButtonStyle.grey)
    async def skills_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_effects, view=SkillsView(weapon=self.weapon, owner=self.owner))




class SkillsView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, weapon: 'Weapon', owner: Union[discord.User, discord.Member]):
        self.weapon = weapon
        self.owner = owner
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label='Main', style=discord.ButtonStyle.grey)
    async def main_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_main, 
                                                 view=WeaponView(weapon=self.weapon, owner=self.owner))
    

    @discord.ui.button(label='Normals', style=discord.ButtonStyle.grey)
    async def normals_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_attacks_normals)


    @discord.ui.button(label='Dodge', style=discord.ButtonStyle.grey)
    async def dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_attacks_dodge)
    

    @discord.ui.button(label='Skill', style=discord.ButtonStyle.grey)
    async def skill_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_attacks_skill)
    

    @discord.ui.button(label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.weapon.embed_attacks_discharge)