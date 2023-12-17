from pydantic import BaseModel


class Users(BaseModel):
    role_id: int
    id: int
    first_name: str  # имя
    middle_name: str  # отчество
    last_name: str  # фамилия
