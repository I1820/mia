![Lamp Project Logo](http://www.googledrive.com/host/0B33KzMHyLoH2eVNHWFJZdmthOVk/Lamp-Logo.png)
# I1820

## Introduction
![I1820 Architecture](http://aolab.github.io/documentation/architecture/I1820.jpg)

I1820 is a improved version of 18.20, it provides you a full featured package that can
do all you need from IoT middleware consist of create notification, collect logs and
discover your thing.  
In I1820 literature you have things and RPi, things are your actuators and sesnors
and RPis are your point of present to I1820, you can merge these two in some type
of devices like ESP8266 and ...  
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

I1820 provides **Sensing Layer** protocols, **Network Layer** and **Interface Layer** for you.

## Basis
Basis of this project comes from [SDN101 project](https://github.com/elahejalalpour/SDN101).  
***Great Memories***

## Contributors
* [Prof. Bahador Bakhshi](http://ceit.aut.ac.ir/~bakhshis/)
* [Iman Tabrizian](https://github.com/Tabrizian)
* [Parham Alvani](http://1995parham.github.io/)

## Development
I think for using this project in development phase,
it's better to use virtual environment:
```sh
pyvenv $PROJECT_ROOT
. $PROJECT_ROOT/bin/activate
$PROJECT_ROOT/run.sh
```

## Up and Running
* Install and Setup InfluxDB
```sh
sudo ./scripts/influxdb-install.sh
influx -execute 'create database I1820'
```
* Install python dependencies
```sh
sudo pip3 install -r requirements.txt
```
* Provide I1820 configuration in YAML ....
```sh
cp I1820/conf/1820.example.yml I1820/conf/I1820.yml
```
* Run :D
```sh
./18.20-serve.py
```
And for API documentation see [here](http://aolab.github.io/I1820/apidoc/).

## Releases

* Orange 1.0.dev1
* Purple 1.0.dev2 [master]
