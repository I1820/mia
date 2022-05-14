[![Travis branch](https://img.shields.io/travis/com/I1820/Core/master.svg?style=flat-square)](https://travis-ci.com/I1820/Core)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/554074dbb573493bbb235d08122e1206)](https://www.codacy.com/app/i1820/Core?utm_source=github.com&utm_medium=referral&utm_content=I1820/Core&utm_campaign=Badge_Grade)

<p align="center"><strong>Good Days Good Things</strong></p>

# I1820, The IoT Platform

- [Introduction](#introduction)
- [Up and Running]('#up-and-running')
- [I1820-UI](https://github.com/AoLab/I1820/blob/master/I1820-UI/README.md)
- [Components](#components)
- [Releases](#releases)
- [ToDo](#todo)

## Introduction

_Next Generation of IoT Platforms_

Middleware connects different, often complex and already existing
programs that were not originally designed to be connected.

I1820 is a improved version of 18.20, it provides you a full featured package
that can do all you need from IoT middleware (Platform) consist of create notification,
collect logs and discover and manage your things.

In I1820 literature you have _things_ and _nodes_, things are your actuators and
sensors and _nodes_ are any device that can connect to the I1820 server,
they only requirement is being able to make MQTT requests. An examples of such
devices are NodeMCU and RPi.

### Why another platform?

The benefits we can point out about I1820 are:

- SDK pain is over, you don't need sdk's anymore!
- Minimalistic dependencies, you're node only should be able to make MQTT
  requests
- Dead simple sample codes
- You can deploy it over your personal PaaS for mission-critical security or high-availability purposes

### I1820 Main Components

I1820 provides following components of **IoT Application Enablement Platform**:

- Connectivity & normalization
- Device management
- Database
- Processing & action management
- Data visualization

## Up and Running

###### in Ubuntu

- **Step 1** Install and Setup InfluxDB \[[InfluxDB installation](https://docs.influxdata.com/influxdb/v1.0/introduction/installation)]

```sh
sudo ./scripts/influxdb-install.sh
influx -execute 'create database I1820'
influx -execute 'create retention policy "a_week" on "I1820" duration 1w replication 1'
```

- **Step 1+** Install and Setup Influx Time-Series-Platform \[[Influx installation](https://github.com/influxdata/chronograf/blob/master/docs/INSTALLATION.md)]

```sh
# Download and Install Kapacitor
wget https://dl.influxdata.com/kapacitor/releases/kapacitor_1.1.0_amd64.deb
sudo dpkg -i kapacitor_1.1.0_amd64.deb

# Start Kapacitor
sudo systemctl start kapacitor

# Verify that Kapacitor is Running
kapacitor list tasks

# Download and Install Telegraf
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.1.1_amd64.deb
sudo dpkg -i telegraf_1.1.1_amd64.deb

# Start Telegraf
sudo systemctl start telegraf

# Download and Install Chronograf
wget https://dl.influxdata.com/chronograf/nightlies/chronograf_nightly_amd64.deb
sudo dpkg -i chronograf_nightly_amd64.deb

# Start Chronograf
sudo systemctl start chronograf

# Let's have fun with influx on http://localhost:8888
```

- **Step 1+** Install and Setup MongoDB

```sh
sudo apt-get install mongodb
```

- **Step 2** Install and Setup eMQTT \[[eMQTT installation](http://emqtt.io/docs/v2/install.html)]

```sh
unzip emqttd-ubuntu64-2.0-beta1-20160830.zip && cd emqttd

# start console
./bin/emqttd console

# start as daemon
./bin/emqttd start

# check status
./bin/emqttd_ctl status

# stop
./bin/emqttd stop
```

- **Step 4** Install python dependencies

```sh
sudo pip3 install -r requirements.txt
```

- **Step 5** Provide I1820 configuration in INI.

```sh
cp I1820/conf/1820.example.ini I1820/conf/1820.ini
```

- **Step 6** Run :rocket:

```sh
./18.20-serve.py
```

## Docker

Let's build our docker image :yum: (WIP)

```sh
sudo docker build --no-cache -t i1820/core .
```

## Components

Thanks to following technologies:

- [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/): Time-Series Data Storage
- [ActiveMQ](http://activemq.apache.org/): The most popular and powerful open source messaging and Integration Patterns server
- [Consul](): ?

## Releases

- Orange 1.0.dev1
- Pink 1.0
- Purple 2.0
- Green 3.0
- Black 4.0
- Dead 5.0: master

## ToDo

### Core

- [x] OSGi Service Model [based on iPOPO]
- [x] Socket.io based user level notification
- [ ] Distributed I1820

### Database

- [x] MongoDB Support
- [ ] MySQLDB Support

### Comminucation

- [ ] CoAP Proxy
- [ ] HTTP Proxy

### Low Level

- [ ] I1820 C Library
- [ ] I1820 TinyOS
- [ ] I1820 RIOT
