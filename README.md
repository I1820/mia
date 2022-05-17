<p align="center"><strong>Good Days Good Things</strong></p>

# I1820, The IoT Platform

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/I1820/mia/ci?label=ci&logo=github&style=flat-square)

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

## Requests

```sh
curl -X POST 127.0.0.1:8080/things -H 'Content-Type: application/json' -d '{
  "agent_id": "dummy",
  "device_id": "0",
  "type": "dummy",
  "states": ["chert"]
}'
```
