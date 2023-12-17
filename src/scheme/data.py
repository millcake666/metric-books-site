from pydantic import BaseModel


class Data(BaseModel):
    met_code: int
    c_code: int
    met_year: str
    met_fond: str
    met_delo: str
    met_page: str
