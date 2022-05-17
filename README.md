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

### Main Components

mia provides following components of **IoT Application Enablement Platform**:

- Connectivity & normalization
- Device management
- Database
- Processing & action management
- Data visualization
