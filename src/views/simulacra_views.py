
import discord

from typing import Optional, TYPE_CHECKING

from src.views.simulacra_buttons import (trait_button_func, home_button_func, weapon_button_func, advanc_button_func, meta_button_func,
                                        abilities_button_func, discharge_button_func, matrice_button_func, weapon_normal_attack_button_func,
                                        weapon_jump_attack_button_func, weapon_dodge_attack_button_func)

if TYPE_CHECKING:
    from src.models.simulacra import Simulacra


class MainView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))


    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''trait Button'''

        await interaction.response.defer()
        em = await trait_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''matrice Button'''

        await interaction.response.defer()
        em = await matrice_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MatriceView(simulacra=self.simulacra))



class TraitView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''matrice Button'''

        await interaction.response.defer()
        em = await matrice_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MatriceView(simulacra=self.simulacra))



class MatriceView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''trait Button'''

        await interaction.response.defer()
        em = await trait_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=TraitView(simulacra=self.simulacra))



class WeaponView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='advancements', label='Advancements', style=discord.ButtonStyle.grey)
    async def advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''advancement button'''
        await interaction.response.defer()
        em = await advanc_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=AdvancView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='meta', label='Meta', style=discord.ButtonStyle.grey)
    async def meta_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''meta / rec pairings button'''
        await interaction.response.defer()
        em = await meta_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MetaView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='attack', label='Attack\'s', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''normal button'''
        await interaction.response.defer()
        em = await weapon_normal_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], view=NormalAttackView(simulacra=self.simulacra))



class AdvancView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))



class MetaView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''home Button'''

        await interaction.response.defer()
        em = await home_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=MainView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))



class NormalAttackView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_jump_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=AeroAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_dodge_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DodgeView(simulacra=self.simulacra))
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], view=SkillView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''discharge Button'''
        await interaction.response.defer()
        em = await discharge_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DischargeView(simulacra=self.simulacra))



class AeroAttackView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon_normal_attack Button'''
        await interaction.response.defer()
        em = await weapon_normal_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=NormalAttackView(simulacra=self.simulacra))
    
    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_dodge_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DodgeView(simulacra=self.simulacra))
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], view=SkillView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''discharge Button'''
        await interaction.response.defer()
        em = await discharge_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DischargeView(simulacra=self.simulacra))



class SkillView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon_normal_attack Button'''
        await interaction.response.defer()
        em = await weapon_normal_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=NormalAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_jump_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=AeroAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_dodge_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DodgeView(simulacra=self.simulacra))
    
    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''discharge Button'''
        await interaction.response.defer()
        em = await discharge_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DischargeView(simulacra=self.simulacra))



class DischargeView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon_normal_attack Button'''
        await interaction.response.defer()
        em = await weapon_normal_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=NormalAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_jump_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=AeroAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_dodge_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DodgeView())
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], view=SkillView(simulacra=self.simulacra))


class DodgeView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra'):
        self.simulacra = simulacra
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=WeaponView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon_normal_attack Button'''
        await interaction.response.defer()
        em = await weapon_normal_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=NormalAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''weapon Button'''
        await interaction.response.defer()
        em = await weapon_jump_attack_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=AeroAttackView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''skill button'''
        await interaction.response.defer()
        em = await abilities_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], view=SkillView(simulacra=self.simulacra))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        '''discharge Button'''
        await interaction.response.defer()
        em = await discharge_button_func(interaction, simulacra=self.simulacra)
        await interaction.message.edit(embeds=[em], attachments=[], view=DischargeView(simulacra=self.simulacra))