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
 
 *** problème 2 : capteur 5 : ligne droite dans l'affichage des courbes: identifier pourquoi ? 
----------------------------------------------------------------------------------------------------------
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
 - Création de toutes les fonctions statistique (maximum ,minimum,  somme, moyenne, ecart-type, covariance, variance , etendue)
----------------------------------------------------------------------------------------------------------
V7 / Stats 2 : 
 - création de l'indice de la fonction indice de corrélation 

 ***Problème 5 : Problème de calcul de la moyenne du au capteur 5 qui s’arrête et manque de valeurs capteur 1 (début) et capteur 4 (fin) : provoque un décalage de la courbe de moyenne.
----------------------------------------------------------------------------------------------------------
V8 : 
- Ajout de « None » sur les valeurs manquantes : capteur 1,5 et 4. 
- Modification de la fonction moyenne pour y inclure une division en lien avec le nombre de valeur. 
- Inclusion dans le programme des fonctions statistiques 
- Optimisation du programme en incluant une boucle pour créer la variable k qui représente le nombre de caractères en moins d’une ligne par rapport à la plus grande ligne (52)
----------------------------------------------------------------------------------------------------------
V9 : 
- Modification de la fonction graph () pour qu’elle utilise : soit la liste complète, soit un intervalle donné. 
- Ajout des inputs qui pose les questions relatives à l’étude des données. 
----------------------------------------------------------------------------------------------------------
V10 : 
- Ajout de la fonction occupation : permet de savoir les débuts et fins des périodes occupés sur l’intervalle étudié.
- Changement de côtés des légendes pour une meilleur lisibilité (aucune solution pour la luminosité, c’est le meilleur emplacement qui a été choisi).
----------------------------------------------------------------------------------------------------------
V11 : 
- Création de la fonction start qui permet de lancer le programme après l’appel du fichier dans PowerShell.
- Création de flèches qui affiche le maximum et le minimum sur les courbes étudiés
- Modification du comptage des valeurs. Le nom d’un booléen était utiliser deux fois sur des fonctions non compatibles.
- Affinage de l’affichage des différentes courbes : placement des flèches maximum et minimum
----------------------------------------------------------------------------------------------------------
V12 : VERSION FINAL !!!!




 
 
 
 
 
 

