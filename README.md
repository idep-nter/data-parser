## General info

Aim of this project is to parse lxc container data from a JSON file and saves them into a PostgreSQL database.

## Setup

- be sure you have Docker and PostgreSQL installed on your system
- check and edit postgres credentials in database.py & main.py

Build new Docker image:
```
$ docker build -t teskalabs-parser . 
```

Create a container from the image and run it:
```
$ docker run --network=host teskalabs-parser
```
