import discord

from discord.ext import commands
from discord import app_commands

from bot.core.views.weapon import WeaponView
from bot.core.service.api import TofAPI

from bot.infra.entitys import Weapon, WeaponSimple, Simulacra, SimulacraSimple


class WeaponCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.API_AUTO = TofAPI(
            simple_model=SimulacraSimple,
            model=Simulacra,
            route='simulacra'
        )
        self.API = TofAPI(
            simple_model=WeaponSimple,
            model=Weapon,
            route='weapons'
        )


    @app_commands.command(name='weapon')
    @app_commands.rename(id='name')
    @app_commands.describe(id='Weapon name')
    @app_commands.checks.bot_has_permissions(send_messages = True, 
                                             view_channel = True, 
                                             external_emojis = True, 
                                             embed_links = True, 
                                             send_messages_in_threads = True, 
                                             attach_files = True)
    async def weapon(self, interaction: discord.Interaction, id: str):
        '''
        Simulacra (aka Mimics) weapons.
        '''

        await interaction.response.defer()

        weapon = await self.API.get(id=id, locale=interaction.locale)

        await interaction.edit_original_response(embed=weapon.embed_main, view=WeaponView(weapon=weapon, owner=interaction.user))


    @weapon.autocomplete(name='id')
    async def weapon_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=simulacra.name, value=simulacra.weaponID) 
            for simulacra in await self.API_AUTO.get_all(locale=interaction.locale) 
            if current.lower() in simulacra.name.lower() and simulacra.weaponID
        ][:25]
    
async def setup(bot: commands.Bot):
    await bot.add_cog(WeaponCog(bot))
