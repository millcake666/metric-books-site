from typing import List
from sqlalchemy import select, delete, update, insert
from database.nasPunkt import NasPunkt
from database.uezd import Uezd
from scheme.nasPunkt import NasPunkt as NasPunktJSON

from service.service import DefaultService


class NasPunktService(DefaultService):

    def get(self):
        data: List[NasPunkt] = self.session.scalars(select(NasPunkt)).all()
        return [
            NasPunktJSON.model_validate(item)
            for item in data
        ]

    def get_by_code(self, np_code: int) -> NasPunktJSON:
        q = select(Uezd).where(NasPunkt.np_code == np_code)
        return self.session.scalars(q).one_or_none()

    def delete(self, u_code: int, np_code: int):
        self.session.execute(delete(NasPunkt).where(Uezd.u_code == u_code and NasPunkt.np_code == np_code))
        self.session.commit()

    def patch(self, u_code: int, np_code: int, np_name: str):
        self.session.execute(
            update(NasPunkt).where(Uezd.u_code == u_code and NasPunkt.np_code == np_code).values(u_code=u_code,
                                                                                                 np_name=np_name))
        self.session.commit()

    def add(self, u_code: int, np_name: str):
        insert_stmt = insert(NasPunkt).values(u_code=u_code, np_name=np_name).returning(NasPunkt.np_code)
        result = self.session.execute(insert_stmt)
        self.session.commit()

        last_inserted_id = result.scalar()
        return last_inserted_id
