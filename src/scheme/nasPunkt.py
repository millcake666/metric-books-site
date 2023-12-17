from pydantic import BaseModel


class NasPunkt(BaseModel):
    u_code: int
    np_code: int
    np_name: str
