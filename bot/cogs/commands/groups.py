import discord
import pytz

from discord import app_commands
from discord.ext import commands
from typing import Literal, Optional
from datetime import datetime
from discord.utils import format_dt


from bot.infra.repository import GuildRepository
from bot.core.views.group_views import GroupWithRolesView, GroupWithoutRolesView
from bot.cogs.errorHandler.customErrors import WrongDatetimeFormat



class GroupsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild_repo = GuildRepository()
        self.group_with_roles = GroupWithRolesView()
        self.group_without_roles = GroupWithoutRolesView()
    
    async def cog_load(self):
        self.bot.add_view(self.group_with_roles)
        self.bot.add_view(self.group_without_roles)
        return await super().cog_load()
    
    config = app_commands.Group(name='config', description='Configurate your server',
                                default_permissions=discord.Permissions(administrator=True),
                                guild_only=True)

    teams = app_commands.Group(name='teams', description='Create your own in-game group',
                               default_permissions=discord.Permissions(administrator=True),
                               guild_only=True)

    
    @config.command(name='role', description='Roles allowed to be mentioned in teams')
    @app_commands.describe(role='Role to enable/disable')
    async def group_config_role(self, interaction: discord.Interaction, role: discord.Role):
        if not interaction.guild:
            return
        
        await interaction.response.defer(ephemeral=True)
        embed = discord.Embed()

        if not role.mentionable:
            embed.colour = discord.Colour.dark_red()
            embed.description = f'{role.mention} needs to be mentionable'

        else:
            guild = await self.guild_repo.get(guild_id=interaction.guild.id)
            embed.colour = discord.Colour.dark_green()

            if not guild.roles:
                guild.roles = [role.id]

            elif role.id in guild.roles:
                guild.roles.remove(role.id)

            else:
                guild.roles.append(role.id)
            
            if len(guild.roles) == 0:
                embed.colour = discord.Colour.dark_purple()
                guild.roles = None
            
            await self.guild_repo.update(guild)

            if guild.roles:
                embed.description = 'Allowed Roles:\n' + '\n'.join([f'<@&{role}>' 
                                                                    for role in guild.roles if interaction.guild.get_role(role)])
            else:
                embed.description = 'Allowed Roles:\nNone'
        
        await interaction.edit_original_response(embed=embed)
    

    @teams.command(name='create', description='Create your in-game team')
    @app_commands.describe(event='Name or Allowed Role', datetime_='dd/mm/yy HH:MM',
                           description='Group extra description', timezone='Timezone to use (default UTC 0)',
                           color='HEX Color (#121212)', level='Minimal level required', gear_score='Minimal gear score required',
                           group_lenght='How much players', group_roles='DPS, Tank, Support and Reserves')
    @app_commands.rename(datetime_='datetime')
    async def team_create_command(self, interaction: discord.Interaction, 
                                  event: str, datetime_: str,
                                  description: Optional[str], color: Optional[str],
                                  level: Optional[int], gear_score: Optional[int], timezone: str = 'UTC',
                                  group_lenght: Optional[int] = None, 
                                  group_roles: Optional[Literal['Yes', 'No']] = 'No',):
        
        if not interaction.guild:
            return

        if event.isdigit():
            role = interaction.guild.get_role(int(event))
            if role:
                content = role.mention
            else:
                content = ''
        else:
            role = None
            content = ''

        try:
            datetime_object = datetime.fromtimestamp(datetime.strptime(datetime_, '%d/%m/%y %H:%M').replace(tzinfo=pytz.timezone(timezone)).timestamp() - 60*6)
        except ValueError:
            raise WrongDatetimeFormat(datetime_, 'dd/mm/yy HH:MM')

        embed = discord.Embed(description=f'*Ends **{format_dt(datetime_object, "f")}**, **{format_dt(datetime_object, "R")}***\n'
                                           '*(the time is automatically converted to your local timezone)*',
                              timestamp=datetime_object)

        embed.set_footer(text=f'{interaction.user.name} - {interaction.user.id}', icon_url=interaction.user.display_avatar)
        
        if description and embed.description:
            embed.description += '\n\n' + description
        
        if role and not color:
            embed.title = role.name
            embed.colour = role.colour

        elif role and color:
            embed.title = role.name
            embed.colour = discord.Colour.from_str(color)

        elif not role and color:
            embed.title = event
            embed.colour = discord.Colour.from_str(color)

        elif not role and not color:
            embed.title = event
            embed.colour = discord.Colour.random()
        
        else:
            embed.title = event
            embed.colour = discord.Colour.random()

        if level:
            embed.title += f' [Lvl: {level}]'
        
        if gear_score:
            embed.title += f' [GS: {gear_score:_}]'.replace('_', '.')

        if group_roles == 'No':
            if group_lenght:
                embed.add_field(name=f'Members - {group_lenght}', value='\u200B')
            else:
                embed.add_field(name='Members', value='\u200B')

            await interaction.response.send_message(content=content, embed=embed, view=GroupWithoutRolesView())
        
        else:
            if group_lenght:
                dps, sup, tank = self.check_group_lenght(group_lenght)

                embed.add_field(name=f'DPS - {dps}', value='\u200B')
                embed.add_field(name=f'SUP - {sup}', value='\u200B')
                embed.add_field(name=f'TANK - {tank}', value='\u200B')
                embed.add_field(name=f'RESERVE - 10', value='\u200B')

            else:
                embed.add_field(name='DPS', value='\u200B')
                embed.add_field(name='SUP', value='\u200B')
                embed.add_field(name='TANK', value='\u200B')
            
            await interaction.response.send_message(content=content, embed=embed, view=GroupWithRolesView())
        
        
        

    def check_group_lenght(self, group_n: int):
        if group_n >= 8:
            return int(group_n * 5/8), int(group_n * 2/8), int(group_n * 1/8)
        else:
            return int(group_n * 2/4), int(group_n * 1/4), int(group_n * 1/4)


    @team_create_command.autocomplete(name='event')
    async def event_or_role_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        if not interaction.guild:
            return []
        
        guild = await self.guild_repo.get(interaction.guild.id)
        if not guild.roles:
            return []

        return [
            app_commands.Choice(name=role.name, value=str(role.id)) 
            for role in [interaction.guild.get_role(role_id) for role_id in guild.roles] 
            if role and (current.lower() in role.name.lower() or current in str(role.id))
        ][:25]

    @team_create_command.autocomplete(name='timezone')
    async def timezone_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=timezone, value=timezone) 
            for timezone in pytz.all_timezones if current.lower() in timezone.lower()
        ][:25]

    
    # @team_create_command.autocomplete(name='channel')
    # async def channel_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    #     if not interaction.guild:
    #         return []
        
    #     guild = await self.guild_repo.get(interaction.guild.id)
    #     if not guild.group_channel:
    #         return []

    #     return [
    #         app_commands.Choice(name=channel.name, value=str(channel.id)) 
    #         for channel in [interaction.guild.get_channel(channel_id) for channel_id in guild.group_channel] 
    #         if channel and (current.lower() in channel.name.lower() or current in str(channel.id))
    #     ][:25]

                

async def setup(bot: commands.Bot):
    await bot.add_cog(GroupsCog(bot))