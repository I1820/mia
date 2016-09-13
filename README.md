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

## RESTFul API
### Read Thing States
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
### Change Thing Settings
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

