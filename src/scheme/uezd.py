from pydantic import BaseModel


class Uezd(BaseModel):
    u_code: int
    u_name: str
