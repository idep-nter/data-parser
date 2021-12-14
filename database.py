import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="postgres",
    )
    connection.autocommit = True
    cursor = connection.cursor()

    create_database_query = """CREATE database container_db;"""
    cursor.execute(create_database_query)
    print("Database was successfully created.")

    create_table_query = """CREATE TABLE containers
              (NAME           TEXT    NOT NULL,
              MEMORY           INTEGER    NOT NULL,
              CPU           INTEGER    NOT NULL,
              CREATED_AT           INTEGER    NOT NULL,
              STATUS           TEXT    NOT NULL,
              IP_ADDRESSES  TEXT[]    NOT NULL);"""
    cursor.execute(create_table_query)
    print("Table was successfully created.")

    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed.")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
