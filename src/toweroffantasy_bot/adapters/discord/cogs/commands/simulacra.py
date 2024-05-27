from toweroffantasy_bot.adapters.discord.embeds.simulacra import profile_embed
from adapters.discord.views.simulacra import SimulacraView
from discord import Interaction
from discord.app_commands import Choice
from discord.ext import commands
from infra.repositories.simulacra import SimulacraRepository
from unidecode import unidecode


class SimulacraCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = SimulacraRepository()

    @commands.hybrid_group(name="simulacra", description="Simulacra group command")
    async def simulacra_group(self, ctx: commands.Context[commands.Bot]):
        pass

    @simulacra_group.command(name="global", description="Simulacra global command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def simulacra_global_command(
        self, ctx: commands.Context[commands.Bot], id: str
    ):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="en", version="global")

        await ctx.reply(
            embeds=profile_embed(data),
            view=SimulacraView(simulacra=data, owner=ctx.author),
        )

    @simulacra_group.command(name="china", description="Simulacra china command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def simulacra_chinese_command(
        self, ctx: commands.Context[commands.Bot], id: str
    ):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await ctx.reply(
            embeds=profile_embed(data),
            view=SimulacraView(simulacra=data, owner=ctx.author),
        )

    @simulacra_global_command.autocomplete(name="id")
    async def simulacra_global_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.repository.get_all_simple(
                lang="en", version="global"
            )
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]

    @simulacra_chinese_command.autocomplete(name="id")
    async def simulacra_chinese_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.repository.get_all_simple(lang="cn", version="china")
            if unidecode(current).lower() in unidecode(data.name).lower()
            or unidecode(current).lower() in data.id.lower()
            or unidecode(current).lower() == data.rarity_string.lower()
        ][:25]


async def setup(bot: commands.Bot):
    await bot.add_cog(SimulacraCog(bot))
