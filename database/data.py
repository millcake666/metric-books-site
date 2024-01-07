from database.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Data(Base):
    __tablename__ = 'Data'

    # met_code = Column(Integer(), primary_key=True, autoincrement=True)
    # c_code = Column(Integer(), ForeignKey('Church.c_code', ondelete='CASCADE'))
    # met_year = Column(Text(), nullable=False)
    # met_fond = Column(Text(), nullable=False)
    # met_delo = Column(Text(), nullable=False)
    # met_page = Column(Text(), nullable=False)
    # church = relationship('Church')

    met_code = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    c_code = Column(Integer(), ForeignKey('Church.c_code', ondelete='CASCADE'), index=True, nullable=False)
    met_year = Column(Text(), nullable=False)
    met_fond = Column(Text(), nullable=False)
    met_delo = Column(Text(), nullable=False)
    met_page = Column(Text(), nullable=False)

    church = relationship('Church')
