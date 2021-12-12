import json

from tinydb import TinyDB
from datetime import datetime, timezone


db = TinyDB("db.json")


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
    Saves data into database.
    """ ""
    for c in data:
        db.insert(
            {
                "name": c["name"],
                "cpu": c["cpu"],
                "memory": c["memory"],
                "created_at": c["created_at"],
                "ip_addresses": c["ip_addresses"],
            }
        )


if __name__ == "__main__":
    main()
