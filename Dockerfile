FROM alpine
MAINTAINER AoLab

EXPOSE 8080

# Install packages
RUN apk --update add python3
RUN apk --update add --virtual build-dependencies gcc musl-dev python3-dev

# Let's Go Home
WORKDIR /home/root

# I1820
WORKDIR /home/root/I1820
COPY . .
RUN pyvenv .
RUn pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Remove packages
RUN apk del build-dependencies

# Cleanup
RUN rm -rf /var/cache/apk/*

# I1820 Configurations
ENV I1820_INFLUXDB_HOST=172.17.0.1

# Entrypoint Script
ENTRYPOINT ["/home/root/I1820/18.20-serve.py"]
