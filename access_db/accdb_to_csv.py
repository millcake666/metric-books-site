import pyodbc
import csv
import os


driver = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')][0]
database_path = os.path.join(os.getcwd(), 'database', 'Gaso.accdb')
csv_save_path = os.path.join(os.getcwd(), 'database', 'csv_export')
tables_name = ['Data', 'Church', 'NasPunkt', 'Uezd']

# 1. Example establish database connection
connection = pyodbc.connect(f'DRIVER={driver};DBQ={database_path};')
cursor = connection.cursor()

for table in tables_name:
    with open(os.path.join(csv_save_path, table + '.csv'), 'w', encoding='utf-8') as file:
        cursor.execute(f'select * from {table};')
        file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
        file_writer.writerow([x[0] for x in cursor.description])

        for row in cursor.fetchall():
            file_writer.writerow(row)

# 4. Close the database connection
cursor.close()
connection.close()

