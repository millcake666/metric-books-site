from typing import List
from sqlalchemy import select, delete, update, insert
from database.nasPunkt import NasPunkt
from database.uezd import Uezd
from database.church import Church

from service.service import DefaultService


class ChurchService(DefaultService):

    def delete(self, np_code: int, c_code: int):
        self.session.execute(
            delete(Church).where(NasPunkt.np_code == np_code and Church.c_code == c_code))
        self.session.commit()

    def patch(self, np_code: int, c_code: int, c_name: str):
        self.session.execute(
            update(Church).where(
                NasPunkt.np_code == np_code and Church.c_code == c_code).values(
                np_code=np_code, c_name=c_name))
        self.session.commit()

    def add(self, np_code: int, c_name: str):
        insert_stmt = insert(Church).values(np_code=np_code, c_name=c_name).returning(Church.c_code)
        result = self.session.execute(insert_stmt)
        self.session.commit()

        last_inserted_id = result.scalar()
        return last_inserted_id
