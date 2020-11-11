# ProjetJulienBrian

Projet d'informatique Julien Cotisson et Brian Delaunay.

A ce jour, voici la liste des avancées du programme :
----------------------------------------------------------------------------------------------------------
V1 : 
 - Extraction des données du fichier csv
 - Convertisseur des dates en secondes par rapport au premier temps de chaque capteur
 - Affichage avec des courbes des 5 données, avec titre, et axes. (Bruit, Température, Humidité, Luminosité, CO2)
 
 *** Problème 1 : Affichage du 6e capteur absent : seuls les 5 premiers sont affichés
----------------------------------------------------------------------------------------------------------
V2 : 
 - Tentative de résolution du problème 1, trouver autre chose
----------------------------------------------------------------------------------------------------------
V3 : 
 - Résolution du problème 1 
----------------------------------------------------------------------------------------------------------
V4 :
 - Optimisation : création d'une liste possédant toutes les données, et chaînes de caractères destinées à l'affichage
 - Fonction graph qui affiche les courbes une par une ou toute en même temps suivant un booléen et la moyenne ou non aussi avec un booléen
 
 *** Problème 2 : capteur 5 : ligne droit dans l'affichage des courbes : identifier pourquoi
 *** Problème 3 : capteur 1 : Décalage pour rapport à tous
----------------------------------------------------------------------------------------------------------
V5 : 
 - Identification du problème 2 : Le capteur 5 s'arrête et reprend plus tard, d'où le "saut"
 - Identification du problème 3 : Le capteur 1 démarre après tous les autres
 - Résolution problème 2 : Ajout de None pour le capteur 5 à la place des valeurs absentes
 - Résolution problème 3 : Ajout de None au début pour le capteur 1 et changement de la date initial du graphique : au lieu de faire démarrer tous les capteurs à leur propre date initale, ils commencent tous à la date la plus antérieure, alias la première du capteur 5
 
 *** Problème 4 : Optimisation à prévoir en vue du très grand nombre de données, et du grand nombre d'opération.
----------------------------------------------------------------------------------------------------------
V6 / Stats :
 - Correction du programme vis à vis de la nouvelle feuille de donnée
 - Création de toutes les fonctions statistiques
 
 
 
 

