# I1820
## Introduction
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
* URL: `/thing/{rpi_id}/{device_id}`
* Method: `POST`
* Request:
```json
{
  "type": "temprature",
  "states": [
    "temprature"
   ]
}
```
#### Change Thing States
* URL: `/thing/{rpi_id}/{device_id}`
* Method: `PUT`
* Request:
```json
{
  "type": "lamp",
  "settings": [
    "on": true
   ]
}
```

