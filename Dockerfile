FROM debian:8

WORKDIR /app

COPY requirements.txt /app

# RUN pip install -r requirements.txt

COPY ./src /app