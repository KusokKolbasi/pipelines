import sqlite3
import csv
import pandas


def get_domain(url):
    return url.split("://")[1].split("/")[0]


def create(table, query, connection='database.db'):
    database = sqlite3.connect(connection)
    database.create_function("url_domain", 1, get_domain)
    database.execute("create table if not exists " + table + " as " + query)
    database.close()
    

def save(file, table, connection='database.db'):
    with open(f"{file}.csv", "w", newline='') as file:
        cursor = sqlite3.connect(connection).cursor()
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'url', 'url_domain'])
        data = cursor.execute("SELECT * FROM " + table)
        writer.writerows(data)


def load(file, table, connection='database.db'):
    database = sqlite3.connect(connection)
    pandas.read_csv(f'{file}').to_sql(name=table, con=database, if_exists='append', index=False)
    database.close()


def execSQL(query, connection='database.db'):
    database = sqlite3.connect(connection)
    database.execute(query)
    database.commit()
    database.close()
    