from typing import List
from sqlalchemy import select, delete, update, insert
from database.data import Data
from scheme.data import Data as DataJSON
from database.church import Church

from service.service import DefaultService


class DataService(DefaultService):
    def get(self, c_code: int):
        data: List[Data] = self.session.scalars(select(Data).where(Church.c_code == c_code)).all()
        return [
            DataJSON.model_validate(item)
            for item in data
        ]

    def delete(self, met_code: int):
        self.session.execute(delete(Data).where(Data.met_code == met_code))
        self.session.commit()

    def patch(self, met_code: int, met_year: str, met_fond: str, met_opis: str, met_delo: str, met_page: str):
        self.session.execute(update(Data).where(Data.met_code == met_code).values(
            met_year=met_year, met_fond=met_fond, met_opis=met_opis, met_delo=met_delo, met_page=met_page))
        self.session.commit()

    def add(self, c_code: int, met_year: str, met_fond: str, met_opis: str, met_delo: str, met_page: str):
        insert_stmt = insert(Data).values(
            c_code=c_code, met_year=met_year, met_fond=met_fond, met_opis=met_opis, met_delo=met_delo,
            met_page=met_page).returning(Data.met_code)
        result = self.session.execute(insert_stmt)
        self.session.commit()

        last_inserted_id = result.scalar()
        return last_inserted_id
