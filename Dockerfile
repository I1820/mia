FROM python:3-alpine

RUN apk add build-base

WORKDIR /app

COPY . .
RUn pip install --upgrade pipenv
RUN pipenv install --system

# cleanup the apk cache
RUN rm -rf /var/cache/apk/*

EXPOSE 8080

# Entrypoint Script
ENTRYPOINT ["python3", "/app/main.py"]
