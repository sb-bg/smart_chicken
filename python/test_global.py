#!/usr/bin/env python
# coding: utf-8

import sys
import time
import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT

# gpio 19 (10) - Sonde T° et HR ext.
DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 10

humid, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
#if humid is None or temp is None:
#	time.sleep(2)
#	continue
print 'EXT. Temperature: {:.1f} °C'.format(temp)
print 'EXT. Humidité:    {:.1f} %'.format(humid)

# gpio 21 (9) - Sonde T° et HR int.
DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 9

humid, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
#if humid is None or temp is None:
#       time.sleep(2)
#       continue
print 'INT. Temperature: {:.1f} °C'.format(temp)
print 'INT. Humidité:    {:.1f} %'.format(humid)


# initialisation
GPIO.setmode(GPIO.BOARD)
# gpio 36 - Carte relais moteur - commande le sens de rotation
GPIO.setup(36, GPIO.OUT, initial=GPIO.HIGH)
# gpio 35 - Carte relais moteur - commande l'arrêt/marche du moteur
GPIO.setup(35, GPIO.OUT, initial=GPIO.HIGH)
# gpio 37 - Fin de course ouverture
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# gpio 38 - Fin de course fermeture
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# gpio 31 - Carte relais option - Lumière
GPIO.setup(31, GPIO.OUT, initial=GPIO.HIGH)
# gpio 32 - Carte relais option - Non affectée
GPIO.setup(32, GPIO.OUT, initial=GPIO.HIGH)
# gpio 13 - Led système
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
# gpio xx - Sonde T° et HR ext.
# gpio xx - Mesure luminosité

# Allumage LED système
print("Allumage LED système")
GPIO.output(13, GPIO.HIGH)

# Test de la lampe
print("Test de la lampe")
GPIO.output(31, GPIO.LOW)
time.sleep(2)
GPIO.output(31, GPIO.HIGH)

# Test du relais option 2
print("Test du relais option 2")
GPIO.output(32, GPIO.LOW)
time.sleep(2)
GPIO.output(32, GPIO.HIGH)

# Test ouverture / fermeture de la porte
def moteur_porte(action):
	etat_ouverture = GPIO.input(37)
	etat_fermeture = GPIO.input(38)
	if action == "ouverture":
		print("Ouverture de la porte")
		if etat_ouverture:
			print("ouverture ee cours")
			while etat_ouverture:
				etat_ouverture = GPIO.input(37)
				GPIO.output(36, GPIO.LOW)
				GPIO.output(35, GPIO.LOW)
			print("Terminé - La porte est ouverte")
			# GPIO.output(35, GPIO.HIGH)
		else:
			print("La porte est déjà ouverte")
	elif action == "fermeture":
		print("Fermeture de la porte")
		if etat_fermeture:
			print("Fermeture en cours")
			while etat_fermeture:
				etat_fermeture = GPIO.input(38)
				GPIO.output(36, GPIO.HIGH)
				GPIO.output(35, GPIO.LOW)
			print("Terminé - La porte est fermée")
			# GPIO.output(35, GPIO.HIGH)
		else:
			print("La porte est déjà fermée")
	else:
		print("Je ne connais pas cette action")


moteur_porte("ouverture")
moteur_porte("fermeture")
moteur_porte("ouverture")
moteur_porte("fermeture")

# Test du haut-parleur

# Test de la caméra

# Extinction LED système
GPIO.output(13, GPIO.LOW)

# Nettoyage du port GPIO
GPIO.cleanup()
