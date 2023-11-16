
from pydantic import BaseModel


class MatriceSet(BaseModel):
    set_2: str
    set_4: str | None