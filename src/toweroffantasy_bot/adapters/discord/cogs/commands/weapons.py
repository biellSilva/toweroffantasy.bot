from adapters.discord.embeds.weapons import stats_embed
from adapters.discord.utils import convert_locale
from adapters.discord.views.weapons import WeaponView
from discord import Interaction, app_commands
from discord.app_commands import Choice
from discord.ext import commands
from infra.cache.weapon import WeaponCache
from infra.repositories.weapon import WeaponRepository
from unidecode import unidecode


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class WeaponCog(
    commands.GroupCog, group_name="weapon", description="Weapon group command"
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.repository = WeaponRepository()
        self.cache = WeaponCache()

    @app_commands.command(name="global", description="Weapon global command")
    async def weapon_global_command(self, interaction: Interaction, id: str):
        await interaction.response.defer()

        data = await self.repository.get(
            id=id, lang=convert_locale(interaction.locale), version="global"
        )

        await interaction.edit_original_response(
            embeds=stats_embed(data), view=WeaponView(data=data, owner=interaction.user)
        )

    @app_commands.command(name="china", description="Weapon china command")
    async def weapon_chinese_command(self, interaction: Interaction, id: str):
        await interaction.response.defer()

        data = await self.repository.get(id=id, lang="cn", version="china")

        await interaction.edit_original_response(
            embeds=stats_embed(data), view=WeaponView(data=data, owner=interaction.user)
        )

    @weapon_global_command.autocomplete(name="id")
    async def weapon_global_autocomplete(
        self, interaction: Interaction, current: str
    ) -> list[Choice[str]]:

        return [
            Choice(name=data.name_with_rarity, value=data.id)
            for data in await self.cache.get_lang(
                lang=convert_locale(interaction.locale), version="global"
            )
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
