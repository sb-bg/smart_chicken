#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import datetime
import Adafruit_DHT

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11

# Sensor connected to Raspberry Pi pin...
DHT_PIN  = 10

humid, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
#if humid is None or temp is None:
#	time.sleep(2)
#	continue
print 'Temperature: {:.1f} °C'.format(temp)
print 'Humidité:    {:.1f} %'.format(humid)
