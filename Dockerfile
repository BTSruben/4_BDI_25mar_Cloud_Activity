FROM python:latest

WORKDIR /root

COPY requirements.txt .
COPY hubble_data.csv .

RUN pip install -r requirements.txt
