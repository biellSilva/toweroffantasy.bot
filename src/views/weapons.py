from collections.abc import Callable
from typing import TYPE_CHECKING

from discord import Embed, Interaction, Member, SelectOption, User
from discord.ui import Select

from src.types import EmojisEnum
from src.utils import convert_to_emoji
from src.views._base import BaseView

if TYPE_CHECKING:
    from src.embeds.weapons import WeaponEmbeds


class WeaponsView(BaseView):
    def __init__(
        self,
        *,
        controller: "WeaponEmbeds",
        timeout: float | None = 180,
        owner: User | Member | None = None,
    ) -> None:
        super().__init__(timeout=timeout, owner=owner)
        self.controller = controller

        self.selector = _SectionSelector(controller)
        self.element_selector = _ElementSelector(controller)
        self.advance_selector = _AdvancementSelector(controller)
        self.skill_selector = _SkillSelector(controller)

        self.add_item(self.selector)

    def remove_selectors(self) -> None:
        self.clear_items()
        self.add_item(self.selector)


class _SectionSelector(Select["WeaponsView"]):
    def __init__(self, controller: "WeaponEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self.controller = controller

        self._options: dict[str, Callable[..., list[Embed]]] = {
            "weapon": controller.main_embed,
            "passives": controller.passives_embed,
            "multi element": controller.multi_element_embed,
            "advancements": controller.advancements_embed,
            "skills": controller.skill_embed,
            "fashions": controller.fashions_embed,
        }

        self.options = [
            SelectOption(label=option.title(), value=option) for option in self._options
        ]

        self.view: "WeaponsView"

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()

        if self.values[0] == "multi element":
            if self.controller.weapon.multi_element:
                self.view.add_item(self.view.element_selector)

            await interaction.edit_original_response(
                embeds=self._options[self.values[0]](), view=self.view
            )
            return

        if self.values[0] == "advancements":
            self.view.add_item(self.view.advance_selector)
            await interaction.edit_original_response(
                embeds=self._options[self.values[0]](), view=self.view
            )
            return

        if self.values[0] == "skills":
            self.view.add_item(self.view.skill_selector)
            await interaction.edit_original_response(
                embeds=self._options[self.values[0]](), view=self.view
            )
            return

        self.view.remove_selectors()

        await interaction.edit_original_response(
            embeds=self._options[self.values[0]](), view=self.view
        )


class _ElementSelector(Select["WeaponsView"]):
    def __init__(self, controller: "WeaponEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self._options: dict[str, list[Embed]] = {
            item.element: controller.multi_element_embed(item.element)
            for item in controller.weapon.multi_element
        }

        self.options = [
            SelectOption(
                label=option.title(), value=option, emoji=convert_to_emoji(option)
            )
            for option in self._options
        ]

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(embeds=self._options[self.values[0]])


class _AdvancementSelector(Select["WeaponsView"]):
    def __init__(self, controller: "WeaponEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self.controller = controller

        self.options = [
            SelectOption(
                label=" ".join(EmojisEnum.DarkStar.value * ind),
                value=str(ind - 1),
            )
            for ind in range(1, len(controller.weapon.advancements) + 1)
        ]

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(
            embeds=self.controller.advancements_embed(int(self.values[0]))
        )


class _SkillSelector(Select["WeaponsView"]):
    def __init__(self, controller: "WeaponEmbeds") -> None:
        super().__init__(min_values=1, max_values=1)

        self.controller = controller

        self.options = [
            SelectOption(
                label=f"{skill.name} [{skill_type.name or skill_type.type}]",
                value=f"{skill_type.type}-{skill.id}",
            )
            for skill_type in controller.weapon.skills
            for skill in skill_type.attacks
        ]

    async def callback(self, interaction: Interaction) -> None:
        await interaction.response.defer()
        await interaction.edit_original_response(
            embeds=self.controller.skill_embed(self.values[0])
        )
