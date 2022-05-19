<h6 align="center">Good Days Good Things</h6>
<h1 align="center">MiA, The IoT Platform</h1>

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/I1820/mia/ci?label=ci&logo=github&style=for-the-badge)
  
## Introduction

_IoT Platform PoC_

Middleware connects different, often complex and already existing
programs that were not originally designed to be connected.

MiA provides you a full featured package
that can do all you need from IoT middleware (Platform) consist of create notification,
collect logs and discover and manage your things.

In MiA literature you have _things_ and _agents_, things are your actuators and
sensors and _agents_ are any device that can connect to the MiA server,
they only requirement is being able to make MQTT requests. An examples of such
devices are NodeMCU and RPi.

### Why another platform?

The benefits we can point out about MiA are:

- SDK pain is over, you don't need sdk's anymore!
- Minimalistic dependencies, you're node only should be able to make MQTT
  requests
- Dead simple sample codes
- You can deploy it over your personal PaaS for mission-critical security or high-availability purposes

### Main Components

MiA provides following components of **IoT Application Enablement Platform**:

- Connectivity & normalization
- Device management
- Database
- Processing & action management
- Data visualization

## Requests

You can use the following reuqest to see the latest data for the given thing.
Please note that in MiA things are uniqued with their `thing_id` and `agent_id`.

```sh
curl -X POST 127.0.0.1:8080/things -H 'Content-Type: application/json' -d '{
  "agent_id": "dummy",
  "device_id": "0",
  "type": "dummy",
  "states": ["chert"]
}'
```
