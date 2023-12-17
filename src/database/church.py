from database.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.data import Data


class Church(Base):
    __tablename__ = 'Church'

    np_code = Column(Integer(), ForeignKey('NasPunkt.np_code'))
    c_code = Column(Integer(), primary_key=True)
    c_name = Column(Text(), nullable=False)
    data = relationship(Data)
