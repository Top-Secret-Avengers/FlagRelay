FROM python:3.12-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="Max Barnes <maxbarnes.dev@gmail.com" \
      version="1.0"

#change this
CMD flask --app=modules/main.py run --host=0.0.0.0 --port=5000 