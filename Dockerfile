FROM python:3

MAINTAINER Michael Sterzinger <michael7sterzinger@gmail.com>

LABEL maintainer="Michael Sterzinger <michael7sterzinger@gmail.com>"
LABEL description="Teskalabs interview task - json data parser"

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD python database.py && python main.py
