from src.api._base import ApiBaseService
from src.models.weapons import Weapon, WeaponSimple


class WeaponService(ApiBaseService[Weapon, WeaponSimple]):
    _PATH = "/weapons"

    def __init__(self) -> None:
        super().__init__(model=Weapon, simple_model=WeaponSimple, path=self._PATH)
