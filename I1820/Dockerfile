FROM alpine
MAINTAINER Iman Tabrizian <tabrizian@outlook.com>

EXPOSE 8080
ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apk update
RUN apk add python3
RUN apk add yaml
RUN apk add git
RUN apk add gcc
RUN apk add python3-dev
RUN apk add musl-dev

# Cleanup
#RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt-get autoremove -y

# Let's Go Home
WORKDIR /home/root

# I1820
RUN git clone https://github.com/aolab/I1820.git
WORKDIR /home/root/I1820
RUN pyvenv . && pip3 install -r requirements.txt

# I1820 Configurations
ENV I1820_INFLUXDB_HOST=172.17.0.1

# Entrypoint Script
ENTRYPOINT ["/home/root/I1820/18.20-serve.py"]
