from database.database import Base, get_session, engine
import os
import csv
from database.church import Church
from database.nasPunkt import NasPunkt
from database.uezd import Uezd
from database.data import Data

# Грузим таблицы в базу
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# quit(0)

# Добавляем значения их csv файлов в базу
session = get_session()

csv_save_path = os.path.join(os.getcwd(), 'database', 'csv_export')

with open(os.path.join(csv_save_path, 'Uezd.csv'), 'r+', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',', lineterminator='\r')
    rows = [row for row in file_reader]
    keys = rows[0]
    rows = rows[1:]

    for row in rows:
        u = Uezd(
            # u_code=row[0],
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
            # np_code=row[1],
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
            # c_code=row[1],
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
            # met_code=row[0],
            c_code=row[1],
            met_year=row[2],
            met_fond=row[3],
            met_delo=row[4],
            met_page=row[5]
        )
        session.add(u)

    session.commit()
