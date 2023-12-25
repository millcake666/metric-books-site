from typing import List

from pydantic import BaseModel


class Church(BaseModel):
    c_code: int
    c_name: str

    class Config:
        from_attributes = True


class NasPunkt(BaseModel):
    np_code: int
    np_name: str
    church: List[Church]

    class Config:
        from_attributes = True


class Uezd(BaseModel):
    u_code: int
    u_name: str
    nas_punkt: List[NasPunkt]

    class Config:
        from_attributes = True
