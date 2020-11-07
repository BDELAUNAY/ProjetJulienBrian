""" Projet Algorithmique et Programation, Groupe B : sujet 2"""

import matplotlib.pyplot as plt

""" Continuer la moyenne (NA), analyser comment utiliser le bol_init_moy (check )"""
""" A termes, enregistrer toutes les listes de capteurs pour les caller sur la même courbe """


def ligne_date(l) : # Fonction qui prend une ligne de base et renvoie la date sous format 'AAAA-MM-JJ HH:MM:SS'
            lg = len(l)
            if lg == 52 :
                return(ligne[26:45])
                
            elif lg == 51 :
                return(ligne[25:44])
                
            elif lg == 50 :
                return(ligne[24:43])
            
            else :
                return(ligne[23:42])
            
def dissociation_date(d) : # date sous format 'AAAA-MM-JJ HH:MM:SS'
    return([int(d[0:4]),int(d[5:7]),int(d[8:10])]) # Renvoie une liste d'entier : [AAAA,MM,JJ]

def convertisseur_HMS(d) : # date sous format 'AAAA-MM-JJ HH:MM:SS'
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
    bruits_moy = [0]*1165
    temp = []
    temp_moy = [0]*1600
    humidity = []
    humidity_moy = [0]*1600
    lum = []
    lum_moy = [0]*1600
    co2 = []
    co2_moy = [0]*1600
    date = []
    ligne = mesures.readline() # Affectation de la première ligne
    i = 2 # Initialisation du compteur de ligne
    date_init_moy = ligne_date(ligne)
    bol_init_moy = True
    count = 0
    count_min = 10000
    while i != 7883 : # Il y a bien 7882 lignes mais on a besoin de retourner une dernière fois dans la boucle pour afficher les dernière courbes.
        if i == 7882 : # Si l'on dépasse le nombre de donnée
            ligne = ['6'] # Cela veut dire qu'on l'on est à la fin donc la condition suivante va être fausse
        if int(ligne[0]) == idd and i != 7882: # Tant que l'id du capteur est bon, on affecte aux listes les valeurs correspondantes 
            i += 1
            bruits.append(float(ligne[2:6]))
            temp.append(float(ligne[7:11]))
            humidity.append(float(ligne[12:16]))
            n = len(ligne)
            if n == 52 : # Le décalage causé par les différentes valeurs de la luminosité impose une disjonction de cas : valeurs de 1 à 4 chiffres
                lum.append(float(ligne[17:21]))
                co2.append(float(ligne[22:25]))
                date.append((ligne[26:45]))
                if bol_init_moy == True and count < 1165 : # Toutes les capteurs n'ont pas le même nombre de donnée, ainsi pour faire une moyenne sur le maximum de valeur, on se cale sur le plus petit nombre de données soit 1165
                    bruits_moy[count] = bruits_moy[count] + float(ligne[2:6])
                    temp_moy[count] = temp_moy[count]+ float(ligne[7:11])
                    humidity_moy[count] = humidity_moy[count] + float(ligne[12:16])
                    lum_moy[count] = lum_moy[count] + float(ligne[17:21])
                    co2_moy[count] = co2_moy[count] + float(ligne[22:25])
                    
                
            elif n == 51 :
                lum.append(float(ligne[17:20]))
                co2.append(float(ligne[21:24]))
                date.append((ligne[25:44]))
                if bol_init_moy == True and count < 1165 :
                    bruits_moy[count] = bruits_moy[count] + float(ligne[2:6])
                    temp_moy[count] = temp_moy[count]+ float(ligne[7:11])
                    humidity_moy[count] = humidity_moy[count] + float(ligne[12:16])
                    lum_moy[count] = lum_moy[count] + float(ligne[17:20])
                    co2_moy[count] = co2_moy[count] + float(ligne[21:24])
                
            elif len(ligne) == 50 :
                lum.append(float(ligne[17:19]))
                co2.append(float(ligne[20:23]))
                date.append((ligne[24:43]))
                if bol_init_moy == True and count < 1165 :
                    bruits_moy[count] = bruits_moy[count] + float(ligne[2:6])
                    temp_moy[count] = temp_moy[count]+ float(ligne[7:11])
                    humidity_moy[count] = humidity_moy[count] + float(ligne[12:16])
                    lum_moy[count] = lum_moy[count] + float(ligne[17:19])
                    co2_moy[count] = co2_moy[count] + float(ligne[20:23])
            
            else :
                lum.append(float(ligne[17:18]))
                co2.append(float(ligne[19:22]))
                date.append((ligne[23:42]))
                if bol_init_moy == True and count < 1165 :
                    bruits_moy[count] += float(ligne[2:6])
                    temp_moy[count] = temp_moy[count]+ float(ligne[7:11])
                    humidity_moy[count] = humidity_moy[count] + float(ligne[12:16])
                    lum_moy[count] = lum_moy[count] + float(ligne[17:18])
                    co2_moy[count] = co2_moy[count] + float(ligne[19:22])
            count += 1
            ligne = mesures.readline() # Affectation de la ligne suivante
            
            
        else : 
            date_init = date[0]
            print(date_init)
            tps = []
            for k in range(len(date)) :
                tps.append(distance_temporelle(date[k])/3600/12)
            plt.title('Relevé du capteur ' + str(idd) + ' : bruit, temprérature et humidité')
            plt.xlabel('Temps en demi_journée')
            plt.ylabel('dB / °C / %')
            plt.xlim(0,30)
            plt.plot(tps,bruits, label = 'Bruit')
            plt.plot(tps,temp, label = 'Température')
            plt.plot(tps,humidity, label = 'Humidité')
            plt.legend(loc='upper left')
            plt.show() # Enlever cette ligne pour supperposer toutes les courbes de chaque capteur
            plt.title('Relevé du capteur ' + str(idd) + ' : Luminosité et CO2 ')
            plt.xlabel('Temps en demi_journée')
            plt.ylabel('Lux / PPM')
            plt.xlim(0,30)
            plt.plot(tps,lum, label = 'Luminosité')
            plt.plot(tps,co2, color = 'r', label = 'CO2')            
            plt.legend(loc='upper left')
            plt.show() # Enlever en plus cette ligne pour superposer toutes les courbes de tous les capteurs
            idd += 1
            bruits = [] # Remise à 0 des listes
            temp = []
            humidity = []
            lum = []
            co2 = []
            date = []
            if count < count_min :
                count_min = count
            if i == 7882 : # Permet de mettre fin à la boucle while
                i += 1
            count = 0

bruits_moy = [i/6 for i in bruits_moy]
print(count_min)
tps = [i*900/3600/12 for i in range(1165)]
test=plt.plot(tps,bruits_moy)

