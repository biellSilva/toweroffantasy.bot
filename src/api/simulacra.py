from src.api._base import ApiBaseService
from src.models.imitation import Imitation


class SimulacraService(ApiBaseService[Imitation]):
    def __init__(self) -> None:
        super().__init__(model=Imitation, path="/simulacra")
