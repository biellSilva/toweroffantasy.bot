from src.api._base import ApiBaseService
from src.models.matrices import Suit, SuitSimple


class MatricesService(ApiBaseService[Suit, SuitSimple]):
    def __init__(self) -> None:
        super().__init__(model=Suit, simple_model=SuitSimple, path="/matrices")
