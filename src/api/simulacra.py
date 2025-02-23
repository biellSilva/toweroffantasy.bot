from src.api._base import ApiBaseService
from src.models.imitation import Imitation, ImitationSimple


class SimulacraService(ApiBaseService[Imitation, ImitationSimple]):
    def __init__(self) -> None:
        super().__init__(
            model=Imitation, simple_model=ImitationSimple, path="/simulacra"
        )
