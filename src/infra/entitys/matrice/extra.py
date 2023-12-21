
from pydantic import BaseModel


class MatrixSet(BaseModel):
    need: int | None
    description: str | None

class MatrixAssets(BaseModel):
    icon: str
    iconLarge: str