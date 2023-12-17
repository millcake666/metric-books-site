from pydantic import BaseModel


class Uezd(BaseModel):
    np_code: int
    c_code: int
    c_name: str
