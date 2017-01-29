<p align="center">
    <img alt="I1820 Logo" src="http://aolab.github.io/I1820/logo/logo-md.png">
</p>

<p align="center"><strong>Good Days Good Things</strong></p>

<p align="center">
    <img alt="Automated Badge" src="https://img.shields.io/docker/automated/aolab/i1820.svg">
    <img alt="Pulls Badge" src="https://img.shields.io/docker/pulls/aolab/i1820.svg">
    <img alt="Build Status" src="https://travis-ci.org/AoLab/I1820.svg?branch=master">
</p>

# I1820
- [Introduction](#introduction)
- [Contributors](#contributers)
- [Up and Running]('#up-and-running')
- [I1820-UI](https://github.com/AoLab/I1820/blob/master/I1820-UI/README.md)
- [Components](#components)
- [Releases](#releases)
- [ToDo](#todo)


## Introduction
*Next Generation of IoT Platforms*

<p align="center"><img alt="I1820 in AoLab IoT Architecture" src="http://aolab.github.io/documentation/architecture/I1820.jpg"></p>

I1820 is a improved version of 18.20, it provides you a full featured package
that can do all you need from IoT middleware (Platform) consist of create notification,
collect logs and discover and manage your things.

In I1820 literature you have *things* and *nodes*, things are your actuators and
sensors and *nodes* are any device that can connect to the I1820 server,
they only requirement is being able to make MQTT requests. An examples of such
devices are NodeMCU and RPi.

### Why another middleware?

The benefits we can point out about I1820 are:

* SDK pain is over, you don't need sdk's anymore!
* Minimalistic dependencies, you're node only should be able to make MQTT
requests
* Dead simple sample codes
* You can deploy it over your personal PaaS for mission-critical security or high-availability purposes

### I1820 Main Components

I1820 provides following components of **IoT Application Enablement Platform**:

* Connectivity & normalization
* Device management
* Database
* Processing & action management
* Data visualization

<p align="center"><img alt="I1820 Main Components" src="http://aolab.github.io/I1820/documentation/I1820-Components.jpg"></p>

## Up and Running
###### in Ubuntu

- **Step 1** Install and Setup InfluxDB \[[InfluxDB installation](https://docs.influxdata.com/influxdb/v1.0/introduction/installation)]

   ```sh
sudo ./scripts/influxdb-install.sh
influx -execute 'create database I1820'
   ```

- **Step 1** Install and Setup Influx Time-Series-Platform \[[Influx installation](https://github.com/influxdata/chronograf/blob/master/docs/INSTALLATION.md)]

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

- **Step 1** Install and Setup MongoDB

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

- **Step 3** Install python dependencies

   ```sh
sudo pip3 install -r requirements.txt
   ```

- **Step 4** Provide I1820 configuration in INI.

   ```sh
cp I1820/conf/1820.example.ini I1820/conf/1820.ini
   ```

- **Step 5** Run :D

   ```sh
./18.20-serve.py
   ```

- **Step 6** API documentation avaiable [here](http://aolab.github.io/I1820-Documentation).


## Components

Thanks to following technologies:

- [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/): Time-Series Data Storage
- [eMQTT](http://emqtt.io/): The Massively Scalable MQTT Broker for IoT and Mobile Applications

## Releases

* Orange 1.0.dev1
* Pink 1.0: [v1.0](https://github.com/AoLab/I1820/tree/v1.0>)
* Purple 2.0
* Green 3.0: master

## ToDo
### Core
- [ ] OSGi Service Model [based on iPOPO]
- [ ] MQTT based user level notification

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
