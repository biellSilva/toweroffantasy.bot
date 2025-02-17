from src.api._base import ApiBaseService
from src.models.matrices import MatrixSuit


class MatricesService(ApiBaseService[MatrixSuit]):
    def __init__(self) -> None:
        super().__init__(model=MatrixSuit, path="/matrices")
