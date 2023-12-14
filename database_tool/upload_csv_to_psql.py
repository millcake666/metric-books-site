from sqlalchemy import create_engine, insert
from sqlalchemy import Table, MetaData, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session, sessionmaker
import csv
import os

# Создаем таблицы в базе
Base = declarative_base()


class Uezd(Base):
    __tablename__ = 'uezd'

    u_code = Column(Integer(), primary_key=True)
    u_name = Column(Text(), nullable=False, unique=True)


class NasPunkt(Base):
    __tablename__ = 'nas_punkt'

    u_code = Column(Integer(), ForeignKey('uezd.u_code'))
    np_code = Column(Integer(), primary_key=True)
    np_name = Column(Text(), nullable=False, unique=True)
    uezd = relationship('Uezd')


class Church(Base):
    __tablename__ = 'church'

    np_code = Column(Integer(), ForeignKey('nas_punkt.np_code'))
    c_code = Column(Integer(), primary_key=True)
    c_name = Column(Text(), nullable=False, unique=True)
    nas_punkt = relationship('NasPunkt')


class Data(Base):
    __tablename__ = 'data'

    met_code = Column(Integer(), primary_key=True)
    c_code = Column(Integer(), ForeignKey('church.c_code'))
    met_year = Column(Text(), nullable=False)
    met_fond = Column(Text(), nullable=False)
    met_delo = Column(Text(), nullable=False)
    met_page = Column(Text(), nullable=False)
    church = relationship('Church')


# Подключение к серверу PostgreSQL на localhost с помощью psycopg2 DBAPI
engine = create_engine("postgresql+psycopg2://admin:admin1234@localhost/metric")
conn = engine.connect()

# Грузим таблицы в базу
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# quit(0)

# Добавляем значения их csv файлов в базу
session = Session(bind=engine)

csv_save_path = os.path.join(os.getcwd(), 'database', 'csv_export')

with open(os.path.join(csv_save_path, 'Uezd.csv'), 'r+', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',', lineterminator='\r')
    rows = [row for row in file_reader]
    keys = rows[0]
    rows = rows[1:]

    for row in rows:
        u = Uezd(
            u_code=row[0],
            u_name=row[1]
        )
        session.add(u)

    session.commit()

with open(os.path.join(csv_save_path, 'NasPunkt.csv'), 'r+', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',', lineterminator='\r')
    rows = [row for row in file_reader]
    keys = rows[0]
    rows = rows[1:]

    for row in rows:
        u = NasPunkt(
            u_code=row[0],
            np_code=row[1],
            np_name=row[2]
        )
        session.add(u)

    session.commit()

with open(os.path.join(csv_save_path, 'Church.csv'), 'r+', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',', lineterminator='\r')
    rows = [row for row in file_reader]
    keys = rows[0]
    rows = rows[1:]

    for row in rows:
        u = Church(
            np_code=row[0],
            c_code=row[1],
            c_name=row[2]
        )
        session.add(u)

    session.commit()

with open(os.path.join(csv_save_path, 'Data.csv'), 'r+', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',', lineterminator='\r')
    rows = [row for row in file_reader]
    keys = rows[0]
    rows = rows[1:]

    for row in rows:
        u = Data(
            met_code=row[0],
            c_code=row[1],
            met_year=row[2],
            met_fond=row[3],
            met_delo=row[4],
            met_page=row[5]
        )
        session.add(u)

    session.commit()
