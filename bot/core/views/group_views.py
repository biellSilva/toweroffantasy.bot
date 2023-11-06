import discord

from typing import Union

from bot.config import EMOJIS



class GroupConfirmView(discord.ui.View):
    def __init__(self, *, timeout: float | None = 180, owner: Union[discord.User, discord.Member], 
                 event: str | discord.Role, embed: discord.Embed, channel: discord.TextChannel):
        self.owner = owner
        self.channel = channel
        self.event = event
        self.embed = embed
        super().__init__(timeout=timeout)

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return

        self.stop()

        await interaction.response.defer()
        await self.channel.send(embed=self.embed)
        await interaction.edit_original_response(content=f'Group sended to {self.channel.mention}', view=None)

    @discord.ui.button(label='Abort', style=discord.ButtonStyle.red)
    async def abort_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if interaction.user != self.owner:
            return
        
        self.stop()
        
        await interaction.response.defer()
        await interaction.edit_original_response(content='Group aborted', view=None)


class GroupWithRolesView(discord.ui.View):
    def __init__(self, *, timeout: float | None = None):
        super().__init__(timeout=timeout)
    

    @discord.ui.button(custom_id='dps', style=discord.ButtonStyle.gray, emoji=EMOJIS.get('dps'))
    async def dps_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        await self.check_button(interaction, button)

    @discord.ui.button(custom_id='sup', style=discord.ButtonStyle.gray, emoji=EMOJIS.get('support'))
    async def sup_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        await self.check_button(interaction, button)
    
    @discord.ui.button(custom_id='tank', style=discord.ButtonStyle.gray, emoji=EMOJIS.get('defense'))
    async def tank_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        await self.check_button(interaction, button)
    
    @discord.ui.button(custom_id='reserve', label='Reserve', style=discord.ButtonStyle.gray)
    async def reservers_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        await self.check_button(interaction, button)

    @discord.ui.button(custom_id='close_team', style=discord.ButtonStyle.red, emoji='✖')
    async def abort_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        
        if not interaction.channel or not interaction.channel.permissions_for(interaction.user).administrator: # type: ignore
            return
        
        if not interaction.message or len(interaction.message.embeds) == 0:
            return
        
        if interaction.message.embeds[0].footer.text and str(interaction.user.id) not in interaction.message.embeds[0].footer.text:
            return
        
        self.stop()
        
        await interaction.response.defer()
        await interaction.edit_original_response(content=f'Group closed by {interaction.user.mention}', view=None)
    
    async def check_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        'checks roles and slots'

        if not interaction.message or len(interaction.message.embeds) == 0:
            return

        await interaction.response.defer()

        for ind, field in enumerate(interaction.message.embeds[0].fields):
            if field.name and field.value and button.custom_id:
                if interaction.user.mention in field.value and button.custom_id in field.name.lower():
                    value = '\n'.join([f'{user_mention}' for user_mention in field.value.split('\n') if user_mention != interaction.user.mention])

                    if len(value) == 0:
                        value = '\u200B' 
                    
                    if '-' in field.name:
                        name, slots = field.name.split('-')
                        embed = interaction.message.embeds[0].set_field_at(ind, name=f'{name.replace(" ", "")} - {int(slots) + 1}', value=value)
                    else:
                        embed = interaction.message.embeds[0].set_field_at(ind, name=field.name, value=value)

                    return await interaction.edit_original_response(embed=embed)
                
                elif interaction.user.mention in field.value and button.custom_id not in field.name.lower():
                    embed = discord.Embed(colour=discord.Colour.dark_red(),
                                          description=f'You are already in **{field.name.split("-")[0]}**\n'
                                                      f'Use the same button to remove your name from it')
                    
                    return await interaction.followup.send(embed=embed, ephemeral=True)
        
        for ind, field in enumerate(interaction.message.embeds[0].fields):
            if field.name and button.custom_id and field.value: 
                if button.custom_id in field.name.lower() and interaction.user.mention not in field.value:
                    value = field.value.replace('\u200B', '') + f'\n{interaction.user.mention}'

                    if '-' in field.name:
                        name, slots = field.name.split('-')

                        if int(slots) <= 0:
                            return interaction.followup.send(ephemeral=True, 
                                                            embed=discord.Embed(
                                                                colour=discord.Colour.dark_red(), 
                                                                description='This field is full'))
                        
                        embed = interaction.message.embeds[0].set_field_at(ind, name=f'{name.replace(" ", "")} - {int(slots) - 1}', value=value)
                    else:
                        embed = interaction.message.embeds[0].set_field_at(ind, name=field.name, value=value)

                    return await interaction.edit_original_response(embed=embed)



class GroupWithoutRolesView(discord.ui.View):
    def __init__(self, *, timeout: float | None = None):
        super().__init__(timeout=timeout)
    

    @discord.ui.button(custom_id='members', label='Enter', style=discord.ButtonStyle.gray)
    async def enter_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):

        if not interaction.message or len(interaction.message.embeds) == 0:
            return

        await interaction.response.defer()

        for ind, field in enumerate(interaction.message.embeds[0].fields):
            if field.value and field.name and button.custom_id and button.custom_id in field.name.lower(): 
                if interaction.user.mention in field.value:
                    value = '\n'.join([f'{user_mention}' for user_mention in field.value.split('\n') if user_mention != interaction.user.mention])

                    if len(value) == 0:
                        value = '\u200B' 
                    
                    if '-' in field.name:
                        name, slots = field.name.split('-')
                        embed = interaction.message.embeds[0].set_field_at(ind, name=f'{name.replace(" ", "")} - {int(slots) + 1}', value=value)
                    else:
                        embed = interaction.message.embeds[0].set_field_at(ind, name=field.name, value=value)

                    return await interaction.edit_original_response(embed=embed)
                
                else:
                    value = field.value.replace('\u200B', '') + f'\n{interaction.user.mention}'

                    if '-' in field.name:
                        name, slots = field.name.split('-')
                        if int(slots) <= 0:
                            return await interaction.followup.send(ephemeral=True, 
                                                                embed=discord.Embed(
                                                                    colour=discord.Colour.dark_red(), 
                                                                    description='This field is full'))
                        
                        embed = interaction.message.embeds[0].set_field_at(ind, name=f'{name.replace(" ", "")} - {int(slots) - 1}', value=value)
                    else:
                        embed = interaction.message.embeds[0].set_field_at(ind, name=field.name, value=value)

                    return await interaction.edit_original_response(embed=embed)
        

    @discord.ui.button(custom_id='close_team', style=discord.ButtonStyle.red, emoji='✖')
    async def abort_button(self, interaction: discord.Interaction, button: discord.ui.Button[discord.ui.View]):
        
        if not interaction.channel or not interaction.channel.permissions_for(interaction.user).administrator: # type: ignore
            return
        
        if not interaction.message or len(interaction.message.embeds) == 0:
            return
        
        if interaction.message.embeds[0].footer.text and str(interaction.user.id) not in interaction.message.embeds[0].footer.text:
            return
        
        self.stop()
        
        await interaction.response.defer()
        await interaction.edit_original_response(content=f'Group closed by {interaction.user.mention}', view=None)