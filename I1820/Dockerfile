FROM ubuntu
MAINTAINER Iman Tabrizian <tabrizian@outlook.com>

EXPOSE 8080

# Install packages
RUN apt-get update
RUN apt-get install -y git && curl
RUN apt-get install -y python3 python3-venv python3-pip python3-dev
RUN apt-get install -y libyaml-dev

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt-get autoremove -y

#
WORKDIR /home/aolab

# I1820
RUN git clone https://github.com/aolab/I1820
WORKDIR /home/aolab/I1820
RUN pyvenv . && pip3 install -r requirements.txt
RUN ./scripts/influxdb-install.sh
RUN influx -execute 'create database I1820'

# Entrypoint Script
ENTRYPOINT ["/home/aolab/I1820/18.20-serve.py"]
