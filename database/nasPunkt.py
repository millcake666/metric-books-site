from database.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.church import Church


class NasPunkt(Base):
    __tablename__ = 'NasPunkt'

    u_code = Column(Integer(), ForeignKey('Uezd.u_code', ondelete='CASCADE'))
    uezd = relationship('Uezd',)
    np_code = Column(Integer(), primary_key=True)
    np_name = Column(Text(), nullable=False)
    church = relationship(Church)
