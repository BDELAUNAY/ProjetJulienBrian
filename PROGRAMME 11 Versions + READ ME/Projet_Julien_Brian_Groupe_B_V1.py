""" Projet Algorithmique et Programation, Groupe B : sujet 2"""

""" Marche pas pour le 6e capteur, à trouver une solution """

import matplotlib.pyplot as plt

def ligne_date(l) : # Fonction qui prend une ligne de base et renvoie la date sous format AAAA-MM-JJ HH:MM:SS
            if n == 52 :
                return(ligne[26:45])
                
            elif n == 51 :
                return(ligne[25:44])
                
            elif len(ligne) == 50 :
                return(ligne[24:43])
            
            else :
                return(ligne[23:42])
            
def dissociation_date(d) : # date sous format AAAA-MM-JJ HH:MM:SS
    return([int(d[0:4]),int(d[5:7]),int(d[8:10])]) # Renvoie une liste d'entier : [AAAA,MM,JJ]

def convertisseur_HMS(d) : # date sous format AAAA-MM-JJ HH:MM:SS
    heure = int(d[11:13])
    minute = int(d[14:16])
    sec = int(d[17:19])
    return( heure * 3600 + minute * 60 + sec ) #Secondes écoulées du jour en cours

def distance_temporelle(d):
    jour_init = dissociation_date(date_init)[2]
    jour_d = dissociation_date(d)[2]
    if jour_d > jour_init :      # Si le jour testé est dans le même mois que l'initial
        return ((jour_d-jour_init-1)*86400 + convertisseur_HMS(d) + 86400-convertisseur_HMS(date_init))
    elif jour_d == jour_init :   # Si les deux jours sont les mêmes
        return (convertisseur_HMS(d)-convertisseur_HMS(date_init))
    else :                       # Si le jour testé est dans le mois suivant
        return(86400-convertisseur_HMS(date_init) + (31 - jour_init + jour_d) * 86400 + convertisseur_HMS(d))

with open("EIVP_KM.csv","r") as mesures : # Ouverture du fichier csv
    mesures.readline() # Saut de la première ligne
    idd = 1
    bruits = [] # Création listes vides
    temp = []
    humidity = []
    lum = []
    co2 = []
    date = []
    ligne = mesures.readline() # Affectation de la première ligne
    i = 2 # Initialisation du compteur de ligne
    while i != 7882 :
        if int(ligne[0]) == idd : # Tant que l'id du capteur est bon, on affecte aux listes les valeurs correspondantes 
            i += 1
            bruits.append(float(ligne[2:6]))
            temp.append(float(ligne[7:11]))
            humidity.append(float(ligne[12:16]))
            n = len(ligne)
            if n == 52 : # Le décalage causé par les différentes valeurs de la luminosité impose une disjonction de cas : valeurs de 1 à 4 chiffres
                lum.append(float(ligne[17:21]))
                co2.append(float(ligne[22:25]))
                date.append((ligne[26:45]))
                
            elif n == 51 :
                lum.append(float(ligne[17:20]))
                co2.append(float(ligne[21:24]))
                date.append((ligne[25:44]))
                
            elif len(ligne) == 50 :
                lum.append(float(ligne[17:19]))
                co2.append(float(ligne[20:23]))
                date.append((ligne[24:43]))
            
            else :
                lum.append(float(ligne[17:18]))
                co2.append(float(ligne[19:22]))
                date.append((ligne[23:42]))
            ligne = mesures.readline() # Affectation de la ligne suivante
            print(i)
            print(idd)
            
        else : 
            date_init = date[0]
            tps = []
            for k in range(len(date)) :
                tps.append(distance_temporelle(date[k])/60)
            plt.title('Relevé du capteur ' + str(idd) + ' : bruit, temprérature et humidité')
            plt.xlabel('Temps en jours')
            plt.ylabel('dB / °C / %')
            plt.xlim(0,20174.15)
            plt.plot(tps,bruits)
            plt.plot(tps,temp)
            plt.plot(tps,humidity)
            plt.show() # Enlever cette ligne pour supperposer toutes les courbes de chaque capteur
            plt.title('Relevé du capteur ' + str(idd) + ' : Luminosité et CO2 ')
            plt.xlabel('Temps en jours')
            plt.ylabel('Lux / PPM')
            plt.xlim(0,20174.15)
            plt.plot(tps,lum)
            plt.plot(tps,co2)
            plt.show() # Enlever en plus cette ligne pour superposer toutes les courbes de tous les capteurs
            idd += 1
            bruits = [] # Remise à 0 des listes
            temp = []
            humidity = []
            lum = []
            co2 = []
            date = []
            print(i)
