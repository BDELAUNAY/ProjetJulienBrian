""" Projet Algorithmique et Programation, Groupe B : sujet 2"""

import matplotlib.pyplot as plt

""" Continuer la moyenne (check), analyser comment utiliser le bol_init_moy (check )"""
""" Mettre les différents éléments : moyenne, max, min, médiane, variance, écart type, étendue..."""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Définition des premières variables"""


cap_moy = [['Bruit Moyen','dB'],['Température Moyen','°C'],['Humidité Moyenne','%'],['Luminosité Moyenne','Lux'],['CO2 Moyen','ppm'],['Temps Moyen','Demi-journées']]
liste_cap = []
for l in range(6) : 
    liste_cap.append([['Bruits','dB'],['Température','°C'],['Humidité','%'],['Luminosité','Lux'],['CO2','ppm'],['Temps','Demi-journées']])
liste_cap.append(cap_moy)
liste_color = ['lime', 'navy', 'crimson', 'darkred', 'dimgray','saddlebrown']
idd = 1
bruits = [] # Création listes vides
bruits_moy = [0]*1165 # 1165 correspond à la plus petit liste
temp = []
temp_moy = [0]*1165
humidity = []
humidity_moy = [0]*1165
lum = []
lum_moy = [0]*1165
co2 = []
co2_moy = [0]*1165
date = []

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Définition des fonctions"""

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

def graph(id_donnee,bol_moy,bol_tous): #Prend en argument deux booléens pour avoir ou non la moyenne avec la donnée d'un ou plusieurs capteur/s 
    if bol_tous == False :
        idd = int(input(" Entrez le numéro du capteur choisi : "))
        plt.title('Relevé du capteur ' + str(idd) + ' : ' + str(liste_cap[idd-1][id_donnee][0]))
        plt.xlabel('Temps en demi_journée')
        plt.ylabel(liste_cap[idd-1][id_donnee][1])
        plt.xlim(0,30)
        plt.plot(liste_cap[idd-1][-1][2],liste_cap[idd-1][id_donnee][2], color = liste_color[0], label = liste_cap[idd-1][id_donnee][0])
        if bol_moy == True :
            plt.plot(tps_moy,liste_cap[-1][id_donnee][2], color = 'darkorange', label = liste_cap[6][id_donnee][0])
        plt.legend(loc='upper left')
        plt.show()
    else : 
        for idd in range(6):
            plt.title('Relevé des capteurs' + ' : ' + str(liste_cap[idd][id_donnee][0]))
            plt.xlabel('Temps en demi_journée')
            plt.ylabel(liste_cap[0][id_donnee][1])
            plt.xlim(0,30)
            plt.plot(liste_cap[idd][-1][2],liste_cap[idd][id_donnee][2], color = liste_color[idd], label = liste_cap[idd][id_donnee][0] + str(idd+1))
            # print(g)
        if bol_moy == True :
            plt.plot(tps_moy,liste_cap[-1][id_donnee][2], color = 'darkorange', label = liste_cap[-1][id_donnee][0])
        plt.legend(loc='upper left')
        plt.show()
        

with open("EIVP_KM.csv","r") as mesures : # Ouverture du fichier csv
    mesures.readline() # Saut de la première ligne
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
            tps = []
            for k in range(len(date)) :
                tps.append(distance_temporelle(date[k])/3600/12)
            liste_donnee=[bruits,temp,humidity,lum,co2,tps]
            k = 0
            for donnee in liste_donnee :
                liste_cap[idd-1][k].append(donnee)
                k += 1
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
temp_moy = [i/6 for i in temp_moy]
humidity_moy = [i/6 for i in humidity_moy]
lum_moy = [i/6 for i in lum_moy]
co2_moy = [i/6 for i in co2_moy]
tps_moy = [i*900/3600/12 for i in range(1165)]

liste_donnee_moy = [bruits_moy,temp_moy,humidity_moy,lum_moy,co2_moy,tps_moy]


for k in range (len(liste_donnee_moy)) :
    liste_cap[-1][k].append(liste_donnee_moy[k])

# print(liste_cap[6])
# for i in range(5):
#     graph(i,True,True)
# for i in range(6):
#     graph(4,True,False)



# for capt in liste_cap :
#     for i in range (5) :
#         print(max(capt[i][2]))









# Calcul du maximum en fonction des capteurs 
for i in range (5) : #varie de 0 1 2 3 4 id des données
    for j in range (6) : #numéro des capteurs
        print("valeur du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :",max(liste_cap[j][i][2]))
        if i==4 and j==5:
            print("\n")

#calcul du minimum e fonction des capteurs
for i in range (5) :
    for j in range (6) :
        print("valeur du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :",min(liste_cap[j][i][2]))
        if i==4 and j==5:
            print ("\n")
            #str() transforme un chiffre en chaîne
#calcul de la médiane
for i in range (5) :
    for j in range (6) :
        print("médiane du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :" + str(len(liste_cap[j][i][2])/2))
        if i==4 and j==5:
            print ("\n")

#calcul de la moyenne des différent capteur
def moyenne () :
    for i in range (5) :
        for j in range (6) :
            somme=0
            for element in liste_cap[j][i][2]:
                somme += element
            print("moyenne du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " : " + str(somme/len(liste_cap[j][i][2]))[:6])
            
moyenne()
            


