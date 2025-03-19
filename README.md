# Car-OBD

###Description du projet

Ce projet réalisé en première année de master est un projet permettant de récupérer des données via la prise OBD (on board diagnostic) de ma voiture, pour ce faire j'ai utilisé une Raspberry Pi 4 ainsi qu'un écran tactile de 5 pouces, pour la communicatyion CAN j'ai utilisé un CAN HAT que j'ai connecté à une prise OBD afin de pouvoir al connecter a la prise de la voiture.

#Matériel précis utilisé :
- RAspberry pi 4 model b 8go
- Ecran Tactile 5 pouces (800*480) waveshare
- CAN HAT RS485 Waveshare
- Prise OBD-II

#Description des Programmes :
- gui.py : Ce programme contient l'entièreté de l'interface graphique ainsi que le programme principal qui permet de faire fonctionner le projet.
- obd.py : Ce programme est la bibliothèque qui a été conçue avec python-can afin de récupérer et convertir les données reçues dde la voiture pour qu'elles soient utilisables dans l'interface graphique du programme gui.py.
- pid_supportes.py : Ce programme permet d'obtenir la liste des identifiants supportés par le véhicule.
