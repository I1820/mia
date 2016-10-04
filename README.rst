I1820
==============================================================================
- `Introduction`_
- `History`_
- `Contributors`_
- `Up and Running`_
- `Releases`_

Introduction
------------------------------------------------------------------------------


.. figure:: http://aolab.github.io/documentation/architecture/I1820.jpg
   :alt: I1820 in AoLab IoT Architecture
   :align: center

I1820 is a improved version of 18.20, it provides you a full featured package
that can do all you need from IoT middleware consist of create notification,
collect logs and discover your things.
In I1820 literature you have things and RPi, things are your actuators and
sesnors and RPis are your point of present to I1820, you can merge these
two in one when you use some type of devices like ESP8266.
When 18.20 decide to leave us alone, we created improved version of it,
in this version we provide everything you need in simple package.

What I1820 Provides for us
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
I1820 provides following services for your IoT platform :)

* Identification Services
* Data Collecting Services

Where I1820 is in IoT Layers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we consider following layers for IoT:

* Sensing Layer
* Network Layer
* Application Layer
* Interface Layer

I1820 provides **Sensing Layer** protocols, **Network Layer**
and **Interface Layer** for you.


History
------------------------------------------------------------------------------
This project had been started as a python REST library for `kaa`_ but after
project grew, we decided to complete it as stand alone middleware. In the
begining we use `SDN101`_ project as a good example of python REST API client.
`SDN101`_ is a **great memory** for `Parham Alvani`_ good old days.
After many weeks of development this project found a new idea from our friend
and developer `Iman Tabrizian`_ and we switched to version 2.

.. _kaa: http://kaaproject.org/
.. _SDN101: https://github.com/eljalalpour/SDN101

Contributors
------------------------------------------------------------------------------
* `Prof. Bahador Bakhshi`_
* `Iman Tabrizian`_
* `Parham Alvani`_

.. _`Parham Alvani`: http://1995parham.github.io/
.. _`Iman Tabrizian`: https://github.com/Tabrizian
.. _`Prof. Bahador Bakhshi`: http://ceit.aut.ac.ir/~bakhshis/

Up and Running
------------------------------------------------------------------------------
1. Install and Setup InfluxDB

   .. code-block:: sh

      sudo ./scripts/influxdb-install.sh
      influx -execute 'create database I1820'

2. Install python dependencies

   .. code-block:: sh

      sudo pip3 install -r requirements.txt

3. Provide I1820 configuration in YAML ....

   .. code-block:: sh

      cp I1820/conf/1820.example.yml I1820/conf/1820.yml

4. [Optional] Initiate Web Interface

   .. code-block:: sh

      git submodule update --init --recursive

5. Run :D

   .. code-block:: sh

      ./18.20-serve.py

6. API documentation avaiable `here <http://aolab.github.io/I1820-Documentation>`_.

Releases
------------------------------------------------------------------------------
* Orange 1.0.dev1
* Pink 1.0
* 2.0 [master]
