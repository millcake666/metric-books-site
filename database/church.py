from database.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.data import Data


class Church(Base):
    __tablename__ = 'Church'

    # np_code = Column(Integer(), ForeignKey('NasPunkt.np_code', ondelete='CASCADE'))
    # c_code = Column(Integer(), primary_key=True, autoincrement=True)
    # c_name = Column(Text(), nullable=False)
    # nasPunkt = relationship('NasPunkt')
    # data = relationship(Data)
    np_code = Column(Integer(), ForeignKey('NasPunkt.np_code', ondelete='CASCADE'), primary_key=True, index=True)
    c_code = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    c_name = Column(Text(), nullable=False)
    nasPunkt = relationship('NasPunkt')
    data = relationship('Data')
