import discord

from time import time

from src.utils import get_git_data, get_ratelimit, get_image ,data_base
from src.config import no_bar


class NamesView(discord.ui.View):

    @discord.ui.button(custom_id='home_help', label='Home', style=discord.ButtonStyle.grey)
    async def home_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        em = interaction.message.embeds[0]
        bot = interaction.client

        git_api = await get_ratelimit()

        start_data_timer = time()
        await get_git_data('yu lan', 'weapons', data_type='json')
        get_data_timer = time() - start_data_timer

        start_image_timer = time()
        await get_image(name=('Yu lan', 'yulan'), data='simulacra')
        get_image_timer = time() - start_image_timer

        em = discord.Embed(color=no_bar,
                            title=f'{bot.user.name} Help',
                            description=f'Status: **{bot.status}** \n'
                                        f'Latency: **{round(bot.latency * 1000)}ms**\n'
                                        f'Data Latency: **{round(get_data_timer * 1000)}ms**\n'
                                        f'Image Latency: **{round(get_image_timer * 1000)}ms**\n'
                                        f'Working on **{len(bot.guilds)} Guilds**')
        
        em.add_field(name='Git Status', value=(f'> Limit: *{git_api.get("limit")}*\n'
                                               f'> Remain: *{git_api.get("remaining")}*\n'
                                               f'> Used: *{git_api.get("used")}*\n'
                                               f'> Reset: <t:{git_api.get("reset")}:R>\n'), inline=False)

        x = ''
        for data_folder, data_list in data_base.items():
            x += f'> {data_folder.title()}: *{len(data_list)} itens*\n' 

        em.add_field(name='Data', value=x, inline=False)

        await interaction.edit_original_response(embed=em, view=NamesView())


    @discord.ui.button(custom_id='commands_help', label='Commands', style=discord.ButtonStyle.grey)
    async def commands_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        em = interaction.message.embeds[0]

        tree = interaction.client.tree
        commands_ = await tree.fetch_commands()

        em.description = ''
        em.clear_fields()
        
        for command in commands_:
            if command.name == 'help':
                continue

            em.description += (f"{command.mention}\n"
                               f"*{command.description}*\n\n")

        await interaction.edit_original_response(embed=em, view=NamesView())

    @discord.ui.button(custom_id='data_help', label='Names', style=discord.ButtonStyle.grey)
    async def data_names_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        em = interaction.message.embeds[0]

        em.description = ''
        em.clear_fields()

        for data_folder in ('simulacra', 'matrices', 'relics', 'smart-servants', 'mounts'):
            data_list = await get_git_data(data_folder=data_folder, data_type='names')
            em.add_field(name=data_folder.title(), value='> '+(', '.join(data_list)), inline=False)

        await interaction.message.edit(embeds=[em], attachments=[], view=NamesView())
    