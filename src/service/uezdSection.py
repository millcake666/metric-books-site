from typing import List
from sqlalchemy import select, delete
from database.uezd import Uezd
from scheme.uezd import Uezd as UezdJSON

from service.service import DefaultService


class UezdSectionService(DefaultService):
    def get(self):
        data: List[Uezd] = self.session.scalars(select(Uezd)).all()
        return [
            UezdJSON.model_validate(item)
            for item in data
        ]

    def get_by_code(self, u_code: int) -> UezdJSON:
        q = select(Uezd).where(Uezd.u_code == u_code)
        return self.session.scalars(q).one_or_none()

    def delete(self, u_code: int):
        self.session.execute(delete(Uezd).where(Uezd.u_code == u_code))
        self.session.commit()
