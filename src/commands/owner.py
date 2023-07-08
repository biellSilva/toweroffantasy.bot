import discord

from discord.ext import commands
from typing import Optional

from src.config import no_bar
from src.utils import get_ratelimit, data_base, get_git_data


class Owner(commands.Cog):

    '''Owner Commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, spec: Optional[str]):
        async with ctx.typing():
            if spec == 'clear':
                ctx.bot.tree.clear_commands()
                await ctx.bot.tree.sync()
                await ctx.reply('commands cleared')

            elif spec == 'data':
                
                git_api = await get_ratelimit()
                if git_api.get("remaining") < 10:
                    return await ctx.reply(f'remaining git api requests: {git_api.get("remaining")} \n reset: <t:{git_api.get("reset")}:R>')
                
                await get_git_data(sync=True)
                
                x = ''
                for data_folder, data_list in data_base.items():
                    x += f'> {data_folder.title()}: *{len(data_list)} itens*\n' 

                em = discord.Embed(color=discord.Colour.dark_embed())
                em.add_field(name='Data', value=x, inline=False)

                await ctx.reply(embed=em)

            else:
                sync = await ctx.bot.tree.sync() 
                await ctx.reply(f'{len(sync)} commands synced')


    @commands.command(name='check')
    @commands.is_owner()
    async def check_bot(self, ctx: commands.Context):
        async with ctx.typing():
            
            git_api = await get_ratelimit()

            em = discord.Embed(color=no_bar,
                               title=f'{self.bot.user}',
                               description=f'Status: **{self.bot.status}** \n'
                                           f'Latency: **{round(self.bot.latency * 1000)}ms**')
            
            em.add_field(name='Git Status', value=(f'> Limit: *{git_api.get("limit")}*\n'
                                                   f'> Remain: *{git_api.get("remaining")}*\n'
                                                   f'> Used: *{git_api.get("used")}*\n'
                                                   f'> Reset: <t:{git_api.get("reset")}:R>\n'), inline=False)
            
            # for future communication if needed
            x = ''
            for guild in self.bot.guilds:
                x += f'> {guild.name}   *{guild.owner}*\n'
                
            em.add_field(name=f'{len(self.bot.guilds)} Guilds', value=x, inline=False)

            x = ''
            for data_folder, data_list in data_base.items():
                x += f'> {data_folder.title()}: *{len(data_list)} itens*\n' 

            em.add_field(name='Data', value=x, inline=False)

            await ctx.send(embed=em)



async def setup(bot):
    await bot.add_cog(Owner(bot))
