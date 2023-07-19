FROM python:3-alpine

RUN apk --no-cache add build-base

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir --upgrade pipenv \
  && pipenv install --system

# cleanup the apk cache
RUN rm -rf /var/cache/apk/*

EXPOSE 8080

# Entrypoint Script
ENTRYPOINT ["python3", "/app/main.py"]
