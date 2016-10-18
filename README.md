<p align="center">
    <img alt="I1820 Logo" src="http://aolab.github.io/I1820/logo/I1820-Logo.jpg">
</p>

<p align="center"><strong>Good Days Good Things</strong></p>

<p align="center">
    <img alt="Automated Badge" src="https://img.shields.io/docker/automated/aolab/i1820.svg">
    <img alt="Pulls Badge" src="https://img.shields.io/docker/pulls/aolab/i1820.svg">
</p>

# I1820
- [Introduction](#introduction)
- [History](#history)
- [Contributors](#contributers)
- [Up and Running]('#up-and-running')
- [I1820-UI](https://github.com/AoLab/I1820/blob/master/I1820-UI/README.md)
- [TaaS is coming ...](#taas-is-coming-)
- [Components](#components)
- [Releases](#releases)


## Introduction
*Next Generation of IoT Platforms*

<p align="center"><img alt="I1820 in AoLab IoT Architecture" src="http://aolab.github.io/documentation/architecture/I1820.jpg"></p>

I1820 is a improved version of 18.20, it provides you a full featured package
that can do all you need from IoT middleware consist of create notification,
collect logs and discover your things.

In I1820 literature you have things and RPi, things are your actuators and
sesnors and RPis are your point of present to I1820, you can merge these
two in one when you use some type of devices like ESP8266.

When 18.20 decide to leave us alone, we created improved version of it,
in this version we provide everything you need in simple package.

### What I1820 Provides for us

I1820 provides following services for your IoT platform :)

* Identification Services
* Data Collecting Services

### Where I1820 is in IoT Layers

If we consider following layers for IoT:

* Sensing Layer
* Network Layer
* Application Layer
* Interface Layer

I1820 provides **Sensing Layer** protocols, **Network Layer**
and **Interface Layer** for you.

### I1820 is different !

In our IoT plafrom you do not have to create any SDK and you can just code
as simple as you think.

### I1820 Main Components

I1820 provides following components of **IoT Application Enablement Platform**:

* Connectivity & normalization
* Device management
* Database
* Processing & action management
* Data visualization


## History

This project had been started as a python REST library for [kaa] but after
project grew, we decided to complete it as stand alone middleware.

In the begining we use [SDN101] project as a good example of python REST API client.
[SDN101] is a **great memory** for [Parham Alvani] good old days.

After many weeks of development this project found a new idea from our friend
and developer [Iman Tabrizian] and we switched to version 2.

[Parham Alvani] had personal issues for using non-GPL packages and protocols
but he finally tried to forget the pass and we finally use [MQTT] protocol and
removed yaml from our project ... version 3.

[kaa]: http://kaaproject.org/
[MQTT]: http://mqtt.org/
[SDN101]: https://github.com/eljalalpour/SDN101

## Contributors

* [Prof. Bahador Bakhshi]
* [Iman Tabrizian]
* [Parham Alvani]

[Parham Alvani]: http://1995parham.github.io/
[Iman Tabrizian]: https://github.com/Tabrizian
[Prof. Bahador Bakhshi]: http://ceit.aut.ac.ir/~bakhshis/

## Up and Running
###### in Ubuntu

1. Install and Setup InfluxDB \[[InfluxDB installation](https://docs.influxdata.com/influxdb/v1.0/introduction/installation)]

   ```sh
sudo ./scripts/influxdb-install.sh
influx -execute 'create database I1820'
   ```

2. Install and Setup eMQTT \[[eMQTT installation](http://emqtt.io/docs/v2/install.html)]

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

3. Install python dependencies

   ```sh
sudo pip3 install -r requirements.txt
   ```

4. Provide I1820 configuration in YAML ....

   ```sh
cp I1820/conf/1820.example.ini I1820/conf/1820.ini
   ```

5. Run :D

   ```sh
./18.20-serve.py
   ```

6. API documentation avaiable [here](http://aolab.github.io/I1820-Documentation).

## [TaaS](https://github.com/AoLab/TaaS) is coming ...

By putting I1820 inside an isolated environment we can put I1820 at scale ...
I1820 instances can be run in diffrent places and work together, TaaS uses this
feature and provides isolated environment for each I1820 and users can use these
environments as a personal IoT platforms.

### Docker for dummies like Parham :(

Zero configuration, zero installation, your IoT middleware is available at your internet speed.
```sh
docker pull aolab/i1820
docker run -d -p 8080:8080 --name="I1820" aolab/i1820
```
and if you want to configure influxDB or MQTT you can do the followings:
```sh
# Detach mode
docker run -d -p 8080:8080 --name="I1820" -e I1820_MQTT_HOST=127.0.0.1 -e I1820_MQTT_PORT=1883 aolab/i1820

# Interactive mode
docker run -ti --rm -p 8080:8080 --name="I1820" -e I1820_MQTT_HOST=127.0.0.1 -e I1820_MQTT_PORT=1883 aolab/i1820
```

### Build

For building the image from scratch:
```sh
docker build -t aolab/i1820 .
```

## Components

Without them we were nothing ...

- [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/): Time-Series Data Storate
- [eMQTT](http://emqtt.io/): The Massively Scalable MQTT Broker for IoT and Mobile Applications

## Releases

* Orange 1.0.dev1
* Pink 1.0: [v1.0](https://github.com/AoLab/I1820/tree/v1.0>)
* Purple 2.0
* Green 3.0: master
