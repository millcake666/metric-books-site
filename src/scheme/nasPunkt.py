from pydantic import BaseModel
from scheme.church import ChurchDict


class NasPunkt(BaseModel):
    u_code: int
    np_code: int
    np_name: str


class NasPunktDict(BaseModel):
    np_name: ChurchDict
