![Lamp Project Logo](http://www.googledrive.com/host/0B33KzMHyLoH2eVNHWFJZdmthOVk/Lamp-Logo.png)
# I1820
## Introduction
![I1820 Architecture](http://aolab.github.io/documentation/architecture/I1820.jpg)

This program does [Kaa](http://www.kaaproject.org/) administration things with CLI
in the first place, I think
using a complex CLI is better than using a simple GUI :D.  
When 18.20 decide to leave us alone, we created improved version of it,
in this version we provide everything you need in simple package.
## Basis
Basis of this project comes from [SDN101 project](https://github.com/elahejalalpour/SDN101).  
***Great Memories***
## Development
I think for using this project in development phase,
it's better to use virtual environment:
```sh
pyvenv $PROJECT_ROOT
. $PROJECT_ROOT/bin/activate
$PROJECT_ROOT/run.sh
```
## Usage :)
### Kaa Environment Setup
### RESTFul API
#### Read Thing States and Status
* URL: `/thing`
* Method: `POST`
* Request:
```json
{
  "type": "temprature",
  "device_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
  "rpi_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
  "states": [
    "temprature"
   ]
}
```
#### Change Thing States
* URL: `/thing`
* Method: `PUT`
* Request:
```json
{
  "type": "lamp",
  "device_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
  "rpi_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
  "settings": {
    "on": true
  }
}
```

