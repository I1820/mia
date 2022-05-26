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

## Up and Running

firs of all you can start the database and mqtt broker (the only requirements for MiA) by provided docker-compose as below:

```sh
docker-compose up -d
```

then you can run MiA with [pipenv](https://pipenv.pypa.io/en/latest/#) as follow:

```sh
pipenv install
pipenv run main.py
```

Also you can the simple dummy agent to check that MiA is up and running:

```
pipenv run dummy.py
```

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

## How to implement an agent?

An _agent_ gather _things_'s data and controls them. Each _agent_ periodically pings the MiA server, so it can find out the agent is up and running and also knows about its current number of active things. Each ping is a message which is sent over MQTT with the following JSON structure and to `I1820/{TENANT_ID}/agent/ping` topic.

```json
"id": "a-very-unique-id",
"things": [
  { "id": "t1", "type": "lamp"  },
],
"actions": []
```

`id` is a unique identification of the _agent_, and it must be set on the agent side (MiA is not a production ready IoT platform, and this is one of its issues). `things` is a list of the active and attached things to the agent. There are no restrictions on how the _agent_ communicate with the things, so you can use SPI, I2C, nRF, Wi-Fi, etc.

Each _thing_ has its `id` but this ID and its _agent_ ID together will unique the _thing_, so you can use the same ID over _things_ that are connected to the different _agents_. Things also has `type`, type specify the things capabilities like what it reports, what it controls etc. Types that are used for things must be defined in MiA and this happens with python files that are [here](https://github.com/I1820/mia/tree/main/I1820/things/models).

Types in the IoT world are very important and there are plenty of things out there so MiA tries its best on the type system which is written in python and without even a restart you can add your types into MiA.

## A Little Bit of History

This platform started as PoC on [AoLab](https://github.com/AoLab) (Summer 2016) when we have many trobble with [Kaa](https://github.com/kaaproject) as our IoT Platform. Our goals were minimizing the resource usage and having a dynamic type system. We used this PoC on Computer Engineering Facility of Amirkabir University of Engineering when we were going to have smart room e2e IoT solution.

After that we planned for having a better and more scalable solution which useful for other IoT verticals beside the smart building and then [I1820](https://github.com/I1820/I1820) borned.
