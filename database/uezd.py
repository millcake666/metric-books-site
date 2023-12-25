from database.database import Base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from database.nasPunkt import NasPunkt


class Uezd(Base):
    __tablename__ = 'Uezd'
    u_code = Column(Integer(), primary_key=True)
    u_name = Column(Text(), nullable=False)
    nas_punkt = relationship(NasPunkt, viewonly=True)
