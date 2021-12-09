import json
import re

from pprint import pprint
from tinydb import TinyDB


db = TinyDB("db.json")


def main():
    with open("sample-data.json") as json_file:
        data = json.load(json_file)
        containers = []

        for c in data:
            try:
                d = {
                    "name": c["name"],
                    "memory": c["state"]["memory"]["usage"],
                    "cpu": c["state"]["cpu"]["usage"],
                    "created_at": c["created_at"],
                    "status": c["status"],
                    "ip_adresses": None,
                }
                # d['ip_adresses'] = getIp(c)
                containers.append(d)

            except TypeError:
                continue

        pprint(containers)
        #saveToDb(containers)


def getIp(nested_dict, prepath=()):
    """
    Search for ip addresses in each container recursively.
    """
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    pass


def saveToDb(data):
    """
    Saves containers data into database.
    """ ""
    pass


if __name__ == "__main__":
    main()
