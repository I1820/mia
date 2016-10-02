I1820
==============================================================================
- :ref:`s1`
- :ref:`s2`
- :ref:`s3`

.. _s1:

Introduction
------------------------------------------------------------------------------

.. image:: http://aolab.github.io/documentation/architecture/I1820.jpg
   :alt: I1820 Architecture
   :align: middle

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


.. _s2:

History
------------------------------------------------------------------------------
This project had been started as a python REST library for `kaa`_ but after
project grew, we decided to complete it as stand alone middleware. In the
begining we use `SDN101`_ project as a good example of python REST API client.
`SDN101`_ is a **great memory** for `Parham Alvani`_ good old days.

.. _kaa: http://kaaproject.org/
.. _SDN101: github.com/eljalalpour/SDN101

.. _s3:

Contributors
------------------------------------------------------------------------------
* `Prof. Bahador Bakhshi`_
* `Iman Tabrizian`_
* `Parham Alvani`_

.. _`Parham Alvani`: http://1995parham.github.io/
.. _`Iman Tabrizian`: https://github.com/Tabrizian
.. _`Prof. Bahador Bakhshi`: http://ceit.aut.ac.ir/~bakhshis/
