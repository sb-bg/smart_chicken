#!/usr/bin/env python
# coding: utf-8

import sys
import time
import RPi.GPIO as GPIO

# initialisation 
GPIO.setmode(GPIO.BOARD)
# Le gpio 36 commande le sens de rotation
GPIO.setup(36, GPIO.OUT, initial=GPIO.HIGH)
# Le gpio 35 commande l'arrêt/marche du moteur
GPIO.setup(35, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if len(sys.argv) != 2:
	print ("Précisez une action en paramètre")
	GPIO.cleanup()
        sys.exit(1)
else:
	action = sys.argv[1]
	etat_ouverture = GPIO.input(37)
	etat_fermeture = GPIO.input(38)

if action == "ouverture":
	print("Ouverture de la porte")
	if etat_ouverture:
		print("Ouverture en cours")
		while etat_ouverture:
			etat_ouverture = GPIO.input(37)
			GPIO.output(36, GPIO.LOW)
			GPIO.output(35, GPIO.LOW)
		print("Terminé - La porte est ouverte")
#		GPIO.output(35, GPIO.HIGH)
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
#		GPIO.output(35, GPIO.HIGH)
	else:
		print("La porte est déjà fermée")
else:
    print("Je ne connais pas cette action")

GPIO.cleanup()
