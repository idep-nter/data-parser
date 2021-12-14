import json
import psycopg2

from psycopg2 import Error
from datetime import datetime, timezone


def main():
    with open("sample-data.json") as json_file:
        data = json.load(json_file)
        container_data = []

        for c in data:
            try:
                d = {
                    "name": c["name"],
                    "memory": c["state"]["memory"]["usage"],
                    "cpu": c["state"]["cpu"]["usage"],
                    "created_at": convertDate(c["created_at"]),
                    "status": c["status"],
                    "ip_addresses": getIp(c),
                }
                container_data.append(d)

            except TypeError:
                continue

        saveToDb(container_data)


def convertDate(date):
    """
    Converts date to UTC timestamp.
    """
    dt = datetime.fromisoformat(date)
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    return timestamp


def getIp(searched_dict):
    """
    Searches recursively for ip addresses in a nested dictionary.
    """
    addresses = []

    for key, value in searched_dict.items():
        if key == "address":
            addresses.append(value)

        elif isinstance(value, dict):
            results = getIp(value)
            for result in results:
                addresses.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = getIp(item)
                    for another_result in more_results:
                        addresses.append(another_result)

    return addresses


def saveToDb(data):
    """
    Inserts data into database.
    """
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="container_db",
        )
        connection.autocommit = True
        cursor = connection.cursor()

        insert_query = """ INSERT INTO containers (NAME, MEMORY, CPU, CREATED_AT, STATUS, IP_ADDRESSES) VALUES (%s, %s, %s, %s, %s, %s)"""
        for c in data:
            container_data = (
                c["name"],
                c["memory"],
                c["cpu"],
                c["created_at"],
                c["status"],
                c["ip_addresses"],
            )
            cursor.execute(insert_query, container_data)
        print("Container data were successfully inserted into database.")

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


if __name__ == "__main__":
    main()
