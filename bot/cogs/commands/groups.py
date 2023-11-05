import discord

from discord import app_commands
from discord.ext import commands
from typing import Literal, Optional

from bot.infra.repository import GuildRepository



class GroupsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild_repo = GuildRepository()
    
    config = app_commands.Group(name='config', description='Configurate your server',
                                default_permissions=discord.Permissions(administrator=True),
                                guild_only=True)

    teams = app_commands.Group(name='teams', description='Create your own in-game group',
                               default_permissions=discord.Permissions(administrator=True),
                               guild_only=True)

    @config.command(name='channel', description='Channels alloweds to be used in teams')
    @app_commands.describe(channel='Text channel to enable/disable')
    async def group_config_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if not interaction.guild:
            return
        
        await interaction.response.defer(ephemeral=True)

        embed = discord.Embed()

        if channel.type != discord.ChannelType.text:
            embed.colour = discord.Colour.dark_red()
            embed.description = f'{channel.mention} needs to be a text channel'

        else:
            guild = await self.guild_repo.get(guild_id=interaction.guild.id)
            embed.colour = discord.Colour.dark_green()

            if not guild.group_channel:
                guild.group_channel = [channel.id]

            elif channel.id in guild.group_channel:
                guild.group_channel.remove(channel.id)

            else:
                guild.group_channel.append(channel.id)
            
            if len(guild.group_channel) == 0:
                embed.colour = discord.Colour.dark_purple()
                guild.group_channel = None
            
            await self.guild_repo.update(guild)

            if guild.group_channel:
                embed.description = 'Allowed Channels:\n' + '\n'.join([f'<#{channel_}>' 
                                                                        for channel_ in guild.group_channel if interaction.guild.get_channel(channel_)])
            else:
                embed.description = 'Allowed Channels:\nNone'
        
        await interaction.edit_original_response(embed=embed)

    
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
    async def team_create_command(self, interaction: discord.Interaction, 
                                  event: str, time: str, 
                                  description: Optional[str], channel: Optional[str],
                                  group_lenght: Optional[app_commands.Range[int, None, 8]] = 0, 
                                  group_roles: Optional[Literal['Yes', 'No']] = 'No'):
        
        if interaction.user.id != self.bot.owner_id:
            raise NotImplementedError
        
        await interaction.response.send_message(content=f'{event} {description} {time} {channel} {group_lenght} {group_roles}')

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
        ]
    
    @team_create_command.autocomplete(name='channel')
    async def channel_autocomplete(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        if not interaction.guild:
            return []
        guild = await self.guild_repo.get(interaction.guild.id)
        if not guild.group_channel:
            return []

        return [
            app_commands.Choice(name=channel.name, value=str(channel.id)) 
            for channel in [interaction.guild.get_channel(channel_id) for channel_id in guild.group_channel] 
            if channel and (current.lower() in channel.name.lower() or current in str(channel.id))
        ]

                

async def setup(bot: commands.Bot):
    await bot.add_cog(GroupsCog(bot))