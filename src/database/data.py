from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Data(Base):
    __tablename__ = 'Data'

    met_code = Column(Integer(), primary_key=True)
    c_code = Column(Integer(), ForeignKey('Church.c_code'))
    met_year = Column(Text(), nullable=False)
    met_fond = Column(Text(), nullable=False)
    met_delo = Column(Text(), nullable=False)
    met_page = Column(Text(), nullable=False)
