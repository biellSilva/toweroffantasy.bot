import discord

from src.utils import get_ratelimit
from src.controller.get_data import get_names


class NamesView(discord.ui.View):

    @discord.ui.button(custom_id='home_help', label='Home', style=discord.ButtonStyle.grey)
    async def home_help_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        em = interaction.message.embeds[0]
        bot = interaction.client

        git_api = await get_ratelimit()

        em = discord.Embed(color=discord.Colour.dark_embed(),
                            title=f'{bot.user.name} Help',
                            description=f'Status: **{bot.status}** \n'
                                        f'Latency: **{round(bot.latency * 1000)}ms**\n'
                                        f'Working on **{len(bot.guilds)} Guilds**')
        
        em.add_field(name='Git Status', value=(f'> Limit: *{git_api.get("limit")}*\n'
                                               f'> Remain: *{git_api.get("remaining")}*\n'
                                               f'> Used: *{git_api.get("used")}*\n'
                                               f'> Reset: <t:{git_api.get("reset")}:R>\n'), inline=False)

        x = (f'> Simulacras: *{len(await get_names("simulacras"))} itens*\n'
             f'> Matrices: *{len(await get_names("matrices"))} itens*\n'
             f'> Relics: *{len(await get_names("relics"))} itens*\n'
             f'> Mounts: *{len(await get_names("mounts"))} itens*\n'
             f'> Smart Servants: *{len(await get_names("smart-servants"))} itens*\n')
        
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

    