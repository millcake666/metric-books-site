from typing import Sequence, Dict

from sqlalchemy import select, desc

from database.uezd import Uezd
from database.nasPunkt import NasPunkt
from database.church import Church
from database.data import Data
from scheme.uezd import UezdDict

from service.service import DefaultService


class DataService(DefaultService):
    def get(self) -> dict:
        ud = UezdDict
        ud.model_dump_json(self.session.scalars(select(NasPunkt)).all())
        res = UezdDict()

        return res
