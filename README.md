<p align="center">
    <img alt="I1820 Logo" src="http://aolab.github.io/I1820/logo/logo-md.png">
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
- [ToDo](#todo)


## Introduction
*Next Generation of IoT Platforms*

<p align="center"><img alt="I1820 in AoLab IoT Architecture" src="http://aolab.github.io/documentation/architecture/I1820.jpg"></p>

I1820 is a improved version of 18.20, it provides you a full featured package
that can do all you need from IoT middleware consist of create notification,
collect logs and discover your things.

In I1820 literature you have *things* and *nodes*, things are your actuators and
sesnors and *nodes* are any device that can connect to the I1820 server, 
they only requirment is being able to make HTTP requests. An examples of such 
devices are NodeMCU and RPi. 

### What I1820 Provides for us

I1820 provides following services:

* Identification Services
* Data Collecting Services

### Why another middleware?

The benefits we can point out about I1820 are:

* SDK pain is over, you don't need sdk's anymore!
* Minimalistic dependencies, you're node only should be able to make HTTP 
requests
* Dead simple sample codes

### I1820 Main Components

I1820 provides following components of **IoT Application Enablement Platform**:

* Connectivity & normalization
* Device management
* Database
* Processing & action management
* Data visualization

<p align="center"><img alt="I1820 Main Components" src="http://aolab.github.io/I1820/documentation/I1820-Components.jpg"></p>


## Contributors

* [Iman Tabrizian]
* [Parham Alvani]

[Parham Alvani]: http://1995parham.github.io/
[Iman Tabrizian]: https://github.com/Tabrizian

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


## Components

Thanks to following technologies:

- [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/): Time-Series Data Storate
- [eMQTT](http://emqtt.io/): The Massively Scalable MQTT Broker for IoT and Mobile Applications

## Releases

* Orange 1.0.dev1
* Pink 1.0: [v1.0](https://github.com/AoLab/I1820/tree/v1.0>)
* Purple 2.0
* Green 3.0: master

## ToDo

[ ] OSGi Service Model [based on iPOPO]
