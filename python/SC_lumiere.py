#!/usr/bin/env python
# coding: utf-8

import sys
import time
import RPi.GPIO as GPIO

# initialisation
GPIO.setmode(GPIO.BOARD)
# Le gpio 31 commande l'option 1 : lumière
GPIO.setup(31, GPIO.OUT, initial=GPIO.HIGH)
# Le gpio 32 commande l'option 2 : non affectée
GPIO.setup(32, GPIO.OUT, initial=GPIO.HIGH)
# Allumage de la lampe
GPIO.output(31, GPIO.LOW)
time.sleep(2)
GPIO.output(31, GPIO.HIGH)
GPIO.cleanup()

