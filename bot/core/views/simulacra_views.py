
import discord

from typing import TYPE_CHECKING, Union

from bot.core.views.simulacra_buttons import *

if TYPE_CHECKING:
    from bot.infra.entitys import Simulacra


class MainView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))


    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''trait Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.trait_embed(), 
                                                 view=TraitView(simulacra=self.simulacra, owner=self.owner))


    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''matrice Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.simulacra.matrice.embed, 
                                                 view=MatriceView(simulacra=self.simulacra, owner=self.owner))



class TraitView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''home Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.simulacra_embed(), view=MainView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='matrice', label='Matrices', style=discord.ButtonStyle.grey)
    async def matrice_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''matrice Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=self.simulacra.matrice.embed, 
                                                 view=MatriceView(simulacra=self.simulacra, owner=self.owner))



class MatriceView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''home Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.simulacra_embed(), view=MainView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))


    @discord.ui.button(custom_id='trait', label='Trait', style=discord.ButtonStyle.grey)
    async def trait_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''trait Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.trait_embed(), 
                                                 view=TraitView(simulacra=self.simulacra, owner=self.owner))




class WeaponView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''home Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.simulacra_embed(), 
                                                 view=MainView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='advancements', label='Advancements', style=discord.ButtonStyle.grey)
    async def advanc_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''advancement button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.advanc_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponBackView(simulacra=self.simulacra, owner=self.owner))


    @discord.ui.button(custom_id='meta', label='Meta', style=discord.ButtonStyle.grey)
    async def meta_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''meta / rec pairings button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.meta_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponBackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='attack', label='Attack\'s', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''normal button'''

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        embed = self.simulacra.weapon.normal_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=NormalAttackView(simulacra=self.simulacra, owner=self.owner))



class WeaponBackView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='home', label='Simulacra', style=discord.ButtonStyle.grey)
    async def home_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''home Button'''

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        await interaction.edit_original_response(embed=await self.simulacra.simulacra_embed(),
                                                 view=MainView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))


class NormalAttackView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon home button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))
        
    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''jump attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.jump_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=AeroAttackView(simulacra=self.simulacra, owner=self.owner))


    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''dodge attack Button'''
        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DodgeView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''skill button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=SkillView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''discharge Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DischargeView(simulacra=self.simulacra, owner=self.owner))



class AeroAttackView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''normal attack button'''

        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        embed = self.simulacra.weapon.normal_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=NormalAttackView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''dodge attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DodgeView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''skill button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=SkillView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''discharge Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DischargeView(simulacra=self.simulacra, owner=self.owner))



class SkillView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''normal attack button'''
        
        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        embed = self.simulacra.weapon.normal_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=NormalAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''jump attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.jump_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=AeroAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''dodge attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DodgeView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''discharge Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DischargeView(simulacra=self.simulacra, owner=self.owner))



class DischargeView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''normal attack button'''
        
        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        embed = self.simulacra.weapon.normal_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=NormalAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''jump attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.jump_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=AeroAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='dodge', label='Dodge', style=discord.ButtonStyle.grey)
    async def weapon_dodge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''dodge attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DodgeView(simulacra=self.simulacra, owner=self.owner))
    
    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''skill button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=SkillView(simulacra=self.simulacra, owner=self.owner))


class DodgeView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, simulacra: 'Simulacra', owner: Union[discord.User, discord.Member]):
        self.simulacra = simulacra
        self.owner = owner
        super().__init__(timeout=timeout)

    @discord.ui.button(custom_id='weapon', label='Weapon', style=discord.ButtonStyle.grey)
    async def weapon_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''weapon Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.main_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=WeaponView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='normal', label='Normal', style=discord.ButtonStyle.grey)
    async def weapon_normal_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''normal attack button'''
        
        if interaction.user != self.owner:
            return
        
        await interaction.response.defer()
        embed = self.simulacra.weapon.normal_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=NormalAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='jump_attack', label='Aerial', style=discord.ButtonStyle.grey)
    async def weapon_aero_attack_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''jump attack Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.jump_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, 
                                                 view=AeroAttackView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='skill', label='Skill', style=discord.ButtonStyle.grey)
    async def abilities_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''skill button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=SkillView(simulacra=self.simulacra, owner=self.owner))

    @discord.ui.button(custom_id='discharge', label='Discharge', style=discord.ButtonStyle.grey)
    async def discharge_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        '''discharge Button'''

        if interaction.user != self.owner:
            return

        await interaction.response.defer()
        embed = self.simulacra.weapon.dodge_embed
        embed.title = self.simulacra.embed_title
        embed.url = self.simulacra.website_url
        await interaction.edit_original_response(embed=embed, view=DischargeView(simulacra=self.simulacra, owner=self.owner))