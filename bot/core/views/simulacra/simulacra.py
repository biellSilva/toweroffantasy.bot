
import discord

from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from bot.infra.entitys import Simulacra


class SimulacraView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)
    

    @discord.ui.button(label='Home', style=discord.ButtonStyle.grey)
    async def main_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embeds=self.simulacra.embed_main)


    @discord.ui.button(label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_trait)

    
    @discord.ui.button(label='Banners', style=discord.ButtonStyle.grey)
    async def banners_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_banners)
    

    @discord.ui.button(label='Info', style=discord.ButtonStyle.grey)
    async def info_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embed=self.simulacra.embed_imitation_info)
    

    @discord.ui.button(label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_main, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))


class WeaponView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        super().__init__(timeout=timeout)
        self.owner = owner
        self.simulacra = simulacra

    @discord.ui.button(label='Back', style=discord.ButtonStyle.grey)
    async def main_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        await interaction.response.defer()

        await interaction.edit_original_response(embeds=self.simulacra.embed_main, 
                                                 view=SimulacraView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(label='Home', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_main)
    
    @discord.ui.button(label='Advancements', style=discord.ButtonStyle.grey)
    async def weapon_advance_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_advanc)

    @discord.ui.button(label='Effects & Attacks', style=discord.ButtonStyle.grey)
    async def weapon_effects_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_effects,
                                                 view=WeaponAttacksView(simulacra=self.simulacra, owner=self.owner))


class WeaponAttacksView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        super().__init__(timeout=timeout)
        self.owner = owner
        self.simulacra = simulacra
    
    @discord.ui.button(label='Back', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_main, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(label='Home', style=discord.ButtonStyle.grey)
    async def weapon_effects_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_effects)
    
    @discord.ui.button(label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_attacks_normals)
    
    @discord.ui.button(label='Jump', style=discord.ButtonStyle.grey)
    async def weapon_jump_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_weapon_attacks_jump)
    
    @discord.ui.button(label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_attacks_dodge)

    @discord.ui.button(label='Skill', style=discord.ButtonStyle.grey)
    async def weapon_skill_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_attacks_skill)
    
    @discord.ui.button(label='Discharge', style=discord.ButtonStyle.grey)
    async def weapon_discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()

        if not self.simulacra.weapon:
            button.disabled = True
            await interaction.edit_original_response(view=self)
            return

        await interaction.edit_original_response(embed=self.simulacra.embed_attacks_discharge)