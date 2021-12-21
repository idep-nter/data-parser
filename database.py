import psycopg2
from psycopg2 import Error


def main():
    try:
        createDB()
        createTable()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def createDB():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        database="postgres",
    )
    connection.autocommit = True
    cursor = connection.cursor()

    create_database_query = """CREATE database container_db;"""
    cursor.execute(create_database_query)
    print("Database was successfully created.")
    cursor.close()
    connection.close()


def createTable():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        database="container_db",
    )
    connection.autocommit = True
    cursor = connection.cursor()

    create_table_query = """CREATE TABLE containers
              (NAME   TEXT    NOT NULL,
              MEMORY    INTEGER    NOT NULL,
              CPU   INTEGER    NOT NULL,
              CREATED_AT    INTEGER    NOT NULL,
              STATUS    TEXT    NOT NULL,
              IP_ADDRESSES    TEXT[]    NOT NULL);"""
    cursor.execute(create_table_query)
    print("Table was successfully created.")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
