""" Projet Algorithmique et Programation, Groupe B : sujet 2"""

import matplotlib.pyplot as plt
import math as mt

""" Continuer la moyenne (check), analyser comment utiliser le bol_init_moy (check )"""
""" Mettre les différents éléments : moyenne, max, min, médiane, variance, écart type, étendue..."""
""" Remplacer le groupe bloc n= 52 ... par une boucle sur les 4 tailles pour que ce soit plus opti (Pas nécessaire)"""
""" Moyenne a faire sur les dernière valeur et sur les valeurs médianes (sans le 5e capteur) """
""" Penser à print les erreurs """
""" Modifier graph() pour qu'elle utilise soit la liste complète ou la liste intervalle en créant une liste qui copie celle à utiliser entre les deux"""
""" Fonction exécuter qui balance tout """

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
liste_etude_cap = []
liste_etude_donnee = []


nb_cap = int(input("Entrez le nombre de capteur à étudier (entre 1 et 6) : "))
for i in range(nb_cap) :
    liste_etude_cap.append(int(input("Quel capteur souhaitez vous étudier ? (Entre 1 et 6, un différent à chaque fois) Le capteur : "))-1)
nb_donnee = int(input("Entrez le nombre de donnée à étudier (entre 1 et 6) : "))
for j in range(nb_donnee) :
    liste_etude_donnee.append(int(input("Quelle donnée souhaitez vous étudier ? Donnez le chiffre correspondant. Dans l'ordre : Bruit, Température, Humidité, Luminosité, CO2, Humidex. Exemple : 4 pour Luminosité. "))-1)
# intervalle = input("Voulez vous étudier cela sur un intervalle donné ? (Oui ou Non) : ")
# bol_intervalle = ( 'Oui' == intervalle)
# if bol_intervalle :
    # date1,date2 = input("Entrez les dates de début et de fin sous la forme : AAAA-MM-JJ HH:MM:SS. Date de début : "),input("Date de fin : ")
date1,date2 = '2019-08-14 12:02:52','2019-08-15 14:15:52'

def indices_intervalle() : # Identifie les indices correspondant à l'intervalle demandé
    tps_debut,tps_fin = distance_temporelle(date1)/3600/12,distance_temporelle(date2)/3600/12
    i_debut = 0
    cap = liste_etude_cap[0]
    while liste_cap[cap][-1][2][i_debut] < tps_debut :
        i_debut += 1
    i_fin = i_debut
    while liste_cap[cap][-1][2][i_fin] < tps_fin :
        i_fin += 1
    return(i_debut,i_fin)


def liste_intervalle() :
    liste = []
    i_debut,i_fin = indices_intervalle()
    i = 0 # i va aller de 0 à nb_cap-1 (indice pour liste, tandis que cap est l'indice pour liste_cap)
    for cap in liste_etude_cap : 
        liste.append([])
        j = 0 # j va aller de 0 à nb_donnee-1 (indice pour liste[i], tandis que donnee est l'indice pour liste_cap[cap])
        for donnee in liste_etude_donnee :
            liste[i].append([])
            liste[i][j].append(liste_cap[cap][donnee][0]) # Ajout du nom de la donnée
            liste[i][j].append(liste_cap[cap][donnee][1]) # Ajout de l'unité
            liste[i][j].append(liste_cap[cap][donnee][2][i_debut:i_fin]) # Ajout des données correspondant à l'intervalle
            j += 1
        liste[i].append([])
        liste[i][-1].append(liste_cap[cap][-1][0]) # De même pour le temps
        liste[i][-1].append(liste_cap[cap][-1][1])
        liste[i][-1].append(liste_cap[cap][-1][2][i_debut:i_fin])
        i += 1
        
    if bol_init_moy == True : # Si on décide d'inclure la courbe moyenne
        liste.append([])
        j = 0
        for donnee in liste_etude_donnee :
            liste[-1].append([])
            liste[-1][j].append(liste_cap[-1][donnee][0]) # Ajout du nom de la donnée
            liste[-1][j].append(liste_cap[-1][donnee][1]) # Ajout de l'unité
            liste[-1][j].append(liste_cap[-1][donnee][2][i_debut:i_fin]) # Ajout des données correspondant à l'intervalle
            j += 1
        liste[-1].append([])
        liste[-1][-1].append(liste_cap[-1][-1][0]) # De même pour le temps
        liste[-1][-1].append(liste_cap[-1][-1][1])
        liste[-1][-1].append(liste_cap[-1][-1][2][i_debut:i_fin])
    return liste

""" Définition des premières variables"""

cap_moy = [['Bruit Moyen','dB'],['Température Moyen','°C'],['Humidité Moyenne','%'],['Luminosité Moyenne','Lux'],['CO2 Moyen','ppm'],['Indice Humidex Moyen',''],['Temps Moyen','Demi-journées']] # Définition du capteur
liste_cap = []
for l in range(6) : 
    liste_cap.append([['Bruits ','dB'],['Température ','°C'],['Humidité ','%'],['Luminosité ','Lux'],['CO2 ','ppm'],['Indice Humidex ',''],['Temps ','Demi-journées']])
liste_cap.append(cap_moy)
# liste_cap sous la forme [cap1,cap2,cap3,cap4,cap5,cap6,cap_moy]
liste_color = ['lime', 'navy', 'crimson', 'darkred', 'dimgray','saddlebrown']
idd = 1
bruits = [] # Création listes vides
bruits_moy = [0]*1345 # 1345 correspond à la taille des listes de données
temp = []
temp_moy = [0]*1345
humidity = []
humidity_moy = [0]*1345
lum = []
lum_moy = [0]*1345
co2 = []
co2_moy = [0]*1345
ind_humidex = []
ind_humidex_moy = [0]*1345
date = []
tps_moy = []


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Tri fusion nécessaire aux analyses statistiques

def fusion(T1,T2) :
    if T1==[] :
        return T2
    if T2==[] :
        return T1
    if T1[0]<T2[0] :
        return [T1[0]]+fusion(T1[1 :],T2)
    else :
        return [T2[0]]+fusion(T1,T2[1 :])

def trifusion(T) :
    if len(T)<=1 : 
        return T
    T1=[T[x] for x in range(len(T)//2)]
    T2=[T[x] for x in range(len(T)//2,len(T))]
    return fusion(trifusion(T1),trifusion(T2))

test = [2,1,7,3,8,4,2,7,9,2,4,6,8,2,4,7,5,1,3,6,5,4,7,5,1,2,5,7,9]

def pop_None(T):
    liste = []
    for element in T :
        if element != None :
            liste.append(element)
    return(liste)

def tri(T):
    liste = pop_None(T)
    return(trifusion(liste))

# CONVERSION DES LIGNES EN LISTE ET CONVERSION TEMPORELLE

def saut_first_col(l) : # Prend en argument une chaîne de caractère composée d'un ';'
    m = 0
    car = l[m]
    while car != ';' :
        m += 1
        car = l[m]
    return(l[m+1:]) # Elle renvoie tout ce qui est après ce point virgule

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
            
def dissociation_date(d) : # d : date sous format 'AAAA-MM-JJ HH:MM:SS'
    return([int(d[0:4]),int(d[5:7]),int(d[8:10])]) # Renvoie une liste d'entier : [AAAA,MM,JJ]

def convertisseur_HMS(d) : # date sous format 'AAAA-MM-JJ HH:MM:SS'
    heure = int(d[11:13])
    minute = int(d[14:16])
    sec = int(d[17:19])
    return( heure * 3600 + minute * 60 + sec ) # Secondes écoulées du jour en cours

def distance_temporelle(d): # d : date sous format 'AAAA-MM-JJ HH:MM:SS'
    jour_init = dissociation_date(date_init)[2]
    jour_d = dissociation_date(d)[2]
    if jour_d > jour_init :      # Si le jour testé est dans le même mois que l'initial
        return ((jour_d-jour_init-1)*86400 + convertisseur_HMS(d) + 86400-convertisseur_HMS(date_init))
    elif jour_d == jour_init :   # Si les deux jours sont les mêmes
        return (convertisseur_HMS(d)-convertisseur_HMS(date_init))
    else :                       # Si le jour testé est dans le mois suivant
        return(86400-convertisseur_HMS(date_init) + (31 - jour_init + jour_d) * 86400 + convertisseur_HMS(d)) # Renvoie donc la distance temporelle entre la date d et la 
    

# ANALYSE DES DONNEES

def valeurs_statistiques(L) :
    M = L[0]
    m = L[0]
    somme_moy = 0
    somme_carre = 0
    for element in L : 
        if M < element : 
            M = element
        if m > element :
            m = element
        somme_moy += element
        somme_carre += element**2

# ANALYSE PHYSIQUE 

a = 17.27
b = 237.7

def alpha(T,phi):
    return(a * T / (b+T) + mt.log(phi))


def humidex(T,phi) :
    temp_rosee = (phi/100)**(1/8)*(112 + 0.9 * T) + 0.1 * T - 112
    return( T + 0.5555 * (6.11 * mt.exp(5417.7530 * (1 / 273.16 - 1 / (273.15 + temp_rosee))) -10))

# def ind_correlation():
#     M = L[0]

def graph(id_donnee,bol_moy,bol_tous): # Prend en argument deux booléens pour avoir ou non la moyenne avec la donnée d'un ou plusieurs capteur/s 
    if bol_tous == False :
        idd = int(input(" Entrez le numéro du capteur choisi : "))
        plt.title('Relevé du capteur ' + str(idd) + ' : ' + str(liste_cap[idd-1][id_donnee][0]))
        plt.xlabel('Temps en demi-journée')
        plt.ylabel(liste_cap[idd-1][id_donnee][1])
        plt.xlim(0,30)
        if idd == 5 :
            plt.plot(liste_cap[idd-1][-1][2],liste_cap[idd-1][id_donnee][2], color = liste_color[0], label = liste_cap[idd-1][id_donnee][0])
        else :
            plt.plot(liste_cap[idd-1][-1][2],liste_cap[idd-1][id_donnee][2], color = liste_color[0], label = liste_cap[idd-1][id_donnee][0])
        if bol_moy == True :
            plt.plot(tps_moy,liste_cap[-1][id_donnee][2], color = 'darkorange', label = liste_cap[-1][id_donnee][0])
        plt.legend(loc='upper left')
        plt.show()
    else : 
        for idd in range(6):
            plt.title('Relevé des capteurs' + ' : ' + str(liste_cap[idd][id_donnee][0]))
            plt.xlabel('Temps en demi_journée')
            plt.ylabel(liste_cap[0][id_donnee][1])
            plt.xlim(0,30)
            plt.plot(liste_cap[idd][-1][2],liste_cap[idd][id_donnee][2], color = liste_color[idd], label = liste_cap[idd][id_donnee][0] + str(idd+1))
        if bol_moy == True :
            plt.plot(tps_moy,liste_cap[-1][id_donnee][2], color = 'darkorange', label = liste_cap[-1][id_donnee][0])
        plt.legend(loc='upper left')
        plt.show()



""" Enregistrement des données dans les listes en vue de faire apparaître les différentes données et diagrammes """

with open("EIVP_KM correction.csv","r") as mesures : # Ouverture du fichier csv
    mesures.readline() # Saut de la première ligne
    ligne = saut_first_col(mesures.readline()) # Affectation de la première ligne
    i = 2 # Initialisation du compteur de ligne
    bol_init_moy = True
    count = 0
    count_min = 10000
    while i != 7883 : # Il y a bien 7882 lignes mais on a besoin de retourner une dernière fois dans la boucle pour afficher les dernière courbes.
        if 984 <= count < 1164 and idd == 5 :
            bol_init_moy = False
        else :
            bol_init_moy = True
        if int(ligne[0]) == idd and bol_init_moy == True : # Tant que l'id du capteur est bon, on affecte aux listes les valeurs correspondantes 
            i += 1
            bruits.append(float(ligne[2:6]))
            temp.append(float(ligne[7:11]))
            humidity.append(float(ligne[12:16]))
            ind_humidex.append(humidex(temp[-1],humidity[-1]))
            k = 52- len(ligne)
            # print(i, len(ligne))
            lum.append(float(ligne[17:21-k]))
            co2.append(float(ligne[22-k:25-k]))
            date.append((ligne[26-k:45-k]))
            bruits_moy[count] = bruits_moy[count] + float(ligne[2:6])
            temp_moy[count] = temp_moy[count]+ float(ligne[7:11])
            humidity_moy[count] = humidity_moy[count] + float(ligne[12:16])
            ind_humidex_moy[count] = ind_humidex_moy[count] + humidex(temp[-1],humidity[-1])
            lum_moy[count] = lum_moy[count] + float(ligne[17:21-k])
            co2_moy[count] = co2_moy[count] + float(ligne[22-k:25-k])
            count += 1
            if i == 7882 : # Si l'on dépasse le nombre de donnée
                ligne = ['7'] # Cela veut dire qu'on l'on est à la fin donc la condition suivante va être fausse
            else :    
                ligne = saut_first_col(mesures.readline()) # Affectation de la ligne suivante
            
        elif int(ligne[0]) == idd and bol_init_moy == False :
            count += 1
        elif int(ligne[0]) != idd :
            print(idd)
            date_init = '2020-09-11 11:30:50' #Date d'allumage du premier capteur (le numéro 5)
            tps = []
            for k in range(len(date)) :
                tps.append(distance_temporelle(date[k])/3600/12)
            liste_donnee=[bruits,temp,humidity,lum,co2,ind_humidex,tps]
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
            ind_humidex = []

            if count < count_min :
                count_min = count
            if i == 7882 : # Permet de mettre fin à la boucle while
                i += 1
            count = 0
            
""" Ajustement des capteurs 1,4 et 5 pour qu'ils aient le même nombre de données que les autres en vue de faire la courbe moyenne"""
""" Toutes les listes de données doivent contenir 1365 éléments soit le nombre maximal de données recensées, notamment par les capteurs 2,3 et 6 """

# Ajustement des données des capteurs
for i in range(6) : 
    
    # Capteur 1 : le capteur 1 commence en retard par rapport aux autres soit à la 9e valeur
    for j in range(9) :
        liste_cap[0][i][2].append(None)
        
    # Capteur 4 : le capteur a une valeur en moins que tous les capteurs car il commence quelques minutes après et les autres et s'éteint quelques minutes avant les autres
    liste_cap[3][i][2].append(None)
    
    # Capteur 5 : le capteur s'arrête au bout de la 984e prise de valeur, et se rallume à la prise de valeur 1164
    liste_cap[4][i][2] = liste_cap[4][i][2][:984] + [None]*180 + liste_cap[4][i][2][984:]


# Ajustement du Temps des capteurs
liste_cap[0][6][2] = [i*15/3600/12 for i in range(9)] + liste_cap[0][6][2]
liste_cap[3][6][2].append(1364*15/3600/12)
liste_cap[4][6][2] = liste_cap[4][6][2][:984] + [i*15/3600/12 for i in range(984,984+180)] + liste_cap[4][6][2][984:]


""" Création de la courbe moyenne """

liste_somme_moy = [bruits_moy,temp_moy,humidity_moy,lum_moy,co2_moy,ind_humidex_moy]
p = 0

# On va diviser les données sommées par le nombre de données sommées car pour les valeurs entre
# 984 et 1164, il n'y a que 5 capteurs fonctionnant donc on divise seulement pas 5 d'où l'utilisation des None
liste_donnee_moy = [[],[],[],[],[],[]]
n = len(liste_donnee_moy)

while p != 1345 :
    for i in range(n) : # Tourne dans les données
        count_none = 0
        for j in range(6) : # Tourne dans les capteurs
            if liste_cap[j][i][2][p] == None :
                count_none += 1
        liste_donnee_moy[i].append(liste_somme_moy[i][p] / (6-count_none))
    p += 1

tps_moy = tps.copy()
liste_donnee_moy.append(tps_moy)
for k in range (len(liste_donnee_moy)) :
    liste_cap[-1][k].append(liste_donnee_moy[k])

graph(4,True,True)



"""test"""