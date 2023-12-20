from pydantic import BaseModel
from scheme.nasPunkt import NasPunktDict


class Uezd(BaseModel):
    u_code: int
    u_name: str


class UezdDict(BaseModel):
    u_name: NasPunktDict
