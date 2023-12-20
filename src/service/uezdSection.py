from typing import List
from sqlalchemy import select
from database.uezd import Uezd
from scheme.uezd import Uezd as UezdJSON, NasPunkt as NPJSON, Church as CRJSON

from service.service import DefaultService


class UezdSectionService(DefaultService):
    def get(self):
        data: List[Uezd] = self.session.scalars(select(Uezd)).all()
        return [
            UezdJSON.model_validate(item)
            for item in data
        ]
