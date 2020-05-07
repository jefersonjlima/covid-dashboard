import argparse
import datetime
import requests
from psycopg2 import connect, Error

parser = argparse.ArgumentParser(description='BRAZILIAN COVID-19 DATABASE ETL.')
parser.add_argument('--version', action='version', version='0.0.1')
args = parser.parse_args()

# COVID-19 Brazil DataBase
URL_BASE = "https://brasil.io" 
FULL_DATA = "/api/dataset/covid19/caso_full/data/"

def parse_first_brewed(text: str) -> datetime.date:
    parts = text.split('/')
    if len(parts) == 2:
        return datetime.date(int(parts[1]), int(parts[0]), 1)
    elif len(parts) == 1:
        return datetime.date(int(parts[0]), 1, 1)
    else:
        assert False, 'Unknown date format'

# TODO: is_repeated,is_last bolean
def create_table(cursor) -> None:
    cursor.execute("""
        DROP TABLE IF EXISTS data;
        CREATE UNLOGGED TABLE data (
            city                                            TEXT,
            city_ibge_code                                  TEXT,
            date                                            DATE,
            epidemiological_week                            INTEGER,
            estimated_population_2019                       INTEGER,
            is_last                                         TEXT,
            is_repeated                                     TEXT,
            last_available_confirmed                        INTEGER,
            last_available_confirmed_per_100k_inhabitants   DECIMAL,
            last_available_date                             DATE,
            last_available_death_rate                       DECIMAL,
            last_available_deaths                           INTEGER,
            new_confirmed                                   INTEGER,
            new_deaths                                      INTEGER,
            order_for_place                                 INTEGER,
            state                                           TEXT
        );""")

# TODO: Poor solution
def insert_one(cursor, values) -> None:
    for value in values:
        #remove states
        str_ibge_code = str(value['city_ibge_code'])
        if len(str_ibge_code) == 7:
            cursor.execute("""
                INSERT INTO data VALUES (
                    %(city)s,
                    %(city_ibge_code)s,
                    %(date)s,
                    %(epidemiological_week)s,
                    %(estimated_population_2019)s,
                    %(is_last)s,
                    %(is_repeated)s,
                    %(last_available_confirmed)s,
                    %(last_available_confirmed_per_100k_inhabitants)s,
                    %(last_available_date)s,
                    %(last_available_death_rate)s,
                    %(last_available_deaths)s,
                    %(new_confirmed)s,
                    %(new_deaths)s,
                    %(order_for_place)s,
                    %(state)s);""",value)
        


def postgres_connection(host = "localhost"):
    try:
        print("PostgreSQL Password: ")
        password = input()
        # declare a new PostgreSQL connection object
        conn = connect(
            dbname = "br_covid",
            user = "metabase",
            host = host,
            password = password,
            # attempt to connect for 3 seconds then raise exception
            connect_timeout = 3
        )
        cur = conn.cursor()
        print ("\ncreated cursor object:", cur)

    except (Exception, Error) as err:
        print ("\npsycopg2 connect error:", err)
        conn = None
        cur = None
    
    return conn, cur

def main():
    conn, cur = postgres_connection()
    assert(conn != None), "postgres connection error"
    create_table(cur)

    try:
        results = []
        PAGE='1'
        while True:
            print(f"Loading Page: {PAGE} ...")
            r = requests.get(url = URL_BASE + FULL_DATA + f"?page={PAGE}")
            data = r.json()
            if data['next']:
                _, PAGE = data['next'].split("?page=")
                insert_one(cur, data['results'])
                conn.commit()
            else: break
    except Exception as e:
        print(f'API brasil.io Error: {e}')


if __name__ == '__main__':
    main()