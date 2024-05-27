from adapters.discord.embeds.matrices import info_embed
from adapters.discord.views.matrices import MatricesView
from discord import Interaction
from discord.app_commands import Choice
from discord.ext import commands
from infra.repositories.matrices import MatricesRepository
from unidecode import unidecode


class MatricesCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = MatricesRepository()

    @commands.hybrid_group(name="matrices", description="Matrices group command")
    async def matrices_group(self, ctx: commands.Context[commands.Bot]):
        pass

    @matrices_group.command(name="global", description="Matrices global command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def matrices_global_command(
        self, ctx: commands.Context[commands.Bot], id: str
    ):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="en", version="global")

        await ctx.reply(
            embeds=info_embed(data),
            view=MatricesView(data=data, owner=ctx.author),
        )

    @matrices_group.command(name="china", description="Matrices china command")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def matrices_chinese_command(
        self, ctx: commands.Context[commands.Bot], id: str
    ):
        if ctx.interaction:
            await ctx.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await ctx.reply(
            embeds=info_embed(data),
            view=MatricesView(data=data, owner=ctx.author),
        )

    @matrices_global_command.autocomplete(name="id")
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

    @matrices_chinese_command.autocomplete(name="id")
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
    await bot.add_cog(MatricesCog(bot))
