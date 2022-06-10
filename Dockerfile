FROM python:3-alpine

RUN apk --update add --virtual build-dependencies

WORKDIR /app

COPY . .
RUn pip install --upgrade pipenv
RUN pipenv install --system

# remove build-time packages
RUN apk del build-dependencies

# cleanup the apk cache
RUN rm -rf /var/cache/apk/*

EXPOSE 8080

# Entrypoint Script
ENTRYPOINT ["python3", "/app/main.py"]
