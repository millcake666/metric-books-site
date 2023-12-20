from sqlalchemy import select

from database.nasPunkt import NasPunkt

from service.service import DefaultService


# class DataService(DefaultService):
#     def get(self) -> dict:
#         ud = UezdDict
#         ud.model_dump_json(self.session.scalars(select(NasPunkt)).all())
#         res = UezdDict()
#
#         return res
