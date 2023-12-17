from typing import Sequence

from sqlalchemy import select, desc

from database.uezd import Uezd
from database.nasPunkt import NasPunkt
from database.church import Church
from database.data import Data

from service.service import DefaultService


class UezdSectionService(DefaultService):
    def get(self) -> Sequence[Uezd]:

        return self.session.scalars(select(Uezd).join(NasPunkt).filter_by(np_code=3)).all()
