import json

from discord.ext import commands
from discord import Embed
from pathlib import Path

from src.utils import ping_db
from src.config import no_bar, matrice_collection, simulacra_collection, db_client


class Owner(commands.Cog):

    '''Owner Commands'''

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='sync')
    @commands.is_owner()
    async def sync(self, ctx: commands.Context):
        async with ctx.typing():
            sync = await ctx.bot.tree.sync()
            await ctx.reply(f'{len(sync)} commands synced')


    @commands.command(name='datasync')
    @commands.is_owner()
    async def datasync(self, ctx: commands.Context):
        async with ctx.typing():
            matrices = Path('./src/database/matrices')
            simulacras = Path('./src/database/simulacra')
            weapons = Path('./src/database/weapons')

            ping = ping_db()

            if ping:
                result = {'simulacra': [], 'matrice':[]}

                db_client.drop_database('glob')

                for simulacra_file in simulacras.iterdir():
                    for weapon_file in weapons.iterdir():
                        if simulacra_file.name.lower() == weapon_file.name.lower():

                            with open(simulacra_file, encoding='utf-8') as f:
                                simulacra_json = json.load(f)

                            with open(weapon_file, encoding='utf-8') as f:
                                weapon_json = json.load(f)

                            simulacra_json['weapon'] = weapon_json

                            simulacra_collection.insert_one(simulacra_json)
                            result['simulacra'].append(simulacra_json['name'])

                for matrice_file in matrices.iterdir():
                    with open(matrice_file, encoding='utf-8') as f:
                        matrice_json = json.load(f)

                    matrice_collection.insert_one(matrice_json)
                    result['matrice'].append(matrice_json['name'])

                em = Embed(color=no_bar, title='Synced')

                for key in result:
                    em.add_field(name=key.capitalize(), value=', '.join(result[key]))

                await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Owner(bot))
