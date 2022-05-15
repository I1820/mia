FROM python:3-alpine

WORKDIR /app

COPY . .
RUN cp I1820/conf/1820.example.ini I1820/conf/1820.ini
RUn pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Remove packages
RUN apk del build-dependencies

# Cleanup
RUN rm -rf /var/cache/apk/*

EXPOSE 8080

# Entrypoint Script
ENTRYPOINT ["/home/root/I1820/18.20-serve.py"]
