from pydantic import BaseModel
from scheme.data import Data


class Church(BaseModel):
    np_code: int
    c_code: int
    c_name: str


class ChurchDict(BaseModel):
    c_name: Data
