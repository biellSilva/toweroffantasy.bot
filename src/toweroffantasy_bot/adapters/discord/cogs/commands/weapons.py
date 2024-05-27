from adapters.discord.embeds.weapons import stats_embed
from adapters.discord.views.weapons import WeaponView
from discord import Interaction
from discord.app_commands import Choice
from discord.ext import commands
from infra.cache.weapon import WeaponCache
from infra.repositories.weapon import WeaponRepository
from unidecode import unidecode


class WeaponCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = WeaponRepository()
        self.cache = WeaponCache()

    @commands.hybrid_group(name="weapon", description="Weapon group command")
    async def weapon_group(self, ctx: commands.Context[commands.Bot]):
        pass

    @weapon_group.command(name="global", description="Weapon global command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def weapon_global_command(self, ctx: commands.Context[commands.Bot], id: str):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="en", version="global")

        await ctx.reply(
            embeds=stats_embed(data), view=WeaponView(data=data, owner=ctx.author)
        )

    @weapon_group.command(name="china", description="Weapon china command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def weapon_chinese_command(
        self, ctx: commands.Context[commands.Bot], id: str
    ):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await ctx.reply(
            embeds=stats_embed(data), view=WeaponView(data=data, owner=ctx.author)
        )

    @weapon_global_command.autocomplete(name="id")
    async def weapon_global_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.cache.get_lang(lang="en", version="global")
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]

    @weapon_chinese_command.autocomplete(name="id")
    async def weapon_chinese_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.cache.get_lang(lang="cn", version="china")
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]


async def setup(bot: commands.Bot):
    await bot.add_cog(WeaponCog(bot))
