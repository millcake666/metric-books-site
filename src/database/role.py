from database import Base
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    users = relationship("Users")
