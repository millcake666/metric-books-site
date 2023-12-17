from sqlalchemy import create_engine, insert
from sqlalchemy import Table, MetaData, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session, sessionmaker
import csv
import os

# Создаем таблицы в базе
Base = declarative_base()


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    users = relationship("Users")


class Users(Base):
    __tablename__ = 'Users'

    role_id = Column(Integer(), ForeignKey('Role.id'))
    id = Column(Integer(), primary_key=True)
    first_name = Column(Text(), nullable=False)  # имя
    middle_name = Column(Text(), nullable=False)  # отчество
    last_name = Column(Text(), nullable=False)  # фамилия


# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://admin:admin1234@localhost/metric")
conn = engine.connect()

# Грузим таблицы в базу
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# quit(0)

# Добавляем значения их csv файлов в базу
session = Session(bind=engine)

session.add_all([
    Role(
        id=0,
        name='Admin'
    ),
    Role(
        id=1,
        name='Editor'
    ),
    Role(
        id=2,
        name='Default'
    )
])
session.commit()

session.add_all([
    Users(
        role_id=0,
        id=0,
        first_name='Dmitry',
        last_name='Gryaznov',
        middle_name='Aleksandrovich'
    ),
    Users(
        role_id=1,
        id=1,
        first_name='Max',
        last_name='Popov',
        middle_name='Vladimirovich'
    ),
    Users(
        role_id=2,
        id=2,
        first_name='Pavel',
        last_name='Morozov',
        middle_name='Ivanovich'
    ),
    Users(
        role_id=2,
        id=3,
        first_name='Default',
        last_name='Default',
        middle_name='Default'
    )
])

session.commit()
