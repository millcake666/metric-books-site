from database.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'Users'

    role_id = Column(Integer(), ForeignKey('Role.id'))
    id = Column(Integer(), primary_key=True)
    first_name = Column(Text(), nullable=False)  # имя
    middle_name = Column(Text(), nullable=False)  # отчество
    last_name = Column(Text(), nullable=False)  # фамилия
