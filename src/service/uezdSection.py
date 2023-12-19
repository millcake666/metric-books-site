from typing import Sequence, Dict

from sqlalchemy import select, desc

from database.uezd import Uezd
from database.nasPunkt import NasPunkt
from database.church import Church
from database.data import Data

from service.service import DefaultService


class UezdSectionService(DefaultService):
    def get(self) -> Sequence[Uezd] | dict:
        uezd_section = self.session.scalars(select(Uezd)).all()
        nas_punkt_section = self.session.scalars(select(NasPunkt)).all()
        church_section = self.session.scalars(select(Church)).all()

        res = dict().fromkeys([key.u_name for key in uezd_section], [])
        for u in uezd_section:
            for np in self.session.scalars(select(NasPunkt).filter_by(u_code=u.u_code)).all():
                res[u.u_name].append(np.np_name)

        print(res)
        return res
