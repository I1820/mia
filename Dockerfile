FROM alpine
MAINTAINER AoLab

EXPOSE 8080

# Install packages
RUN apk update
RUN apk add python3
RUN apk add gcc
RUN apk add musl-dev
RUN apk add python3-dev

# Cleanup
RUN rm -rf /var/cache/apk/*

# Let's Go Home
WORKDIR /home/root

# I1820
WORKDIR /home/root/I1820
COPY . .
RUN pyvenv .
RUn pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Remove packages
RUN apk del gcc
RUN apk del python3-dev
RUN apk del musl-dev

# I1820 Configurations
ENV I1820_INFLUXDB_HOST=172.17.0.1

# Entrypoint Script
ENTRYPOINT ["/home/root/I1820/18.20-serve.py"]
