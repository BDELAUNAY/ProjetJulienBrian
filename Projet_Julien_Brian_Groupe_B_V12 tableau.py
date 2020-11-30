""" Projet Algorithmique et Programation, Groupe B : sujet 2"""

import sys
import matplotlib.pyplot as plt
import math as mt
# import matplotlib.patches as pt

# A faire

""" Continuer la moyenne (check), analyser comment utiliser le bol_init_moy (Check )"""
""" Mettre les différents éléments : moyenne, max, min, médiane, variance, écart type, étendue...(Check)"""
""" Remplacer le groupe bloc n= 52 ... par une boucle sur les 4 tailles pour que ce soit plus opti (Check)"""
""" Moyenne a faire sur les dernière valeur et sur les valeurs médianes (sans le 5e capteur) (check)"""
""" Modifier graph() pour qu'elle utilise soit la liste complète ou la liste intervalle en créant une liste qui copie celle à utiliser entre les deux (check)"""
""" Fonction exécuter qui balance tout (check)"""
""" Modifier graph (check)"""
""" Ajouter les stats """
""" Print l'indice de corrélation (check)"""
""" Affiner l'affichage et finir pour tous les cas(check)"""
""" Fusionner graph int et cap """
""" Tableau des valeurs """
""" Assurer la continuité avec les ordres possibles"""
""" EN GROS FAIRE LA FONCTION START() et c'est fini !!!!!!!!!!"""
""" Mettre des None si l'intervalle prend dans les mauvais temps """
"""ERREURS A METTRE"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Définition des premières variables"""

cap_moy = [['Bruit Moyen','dB'],['Température Moyen','°C'],['Humidité Moyenne','%'],['Luminosité Moyenne','Lux'],['CO2 Moyen','ppm'],['Indice Humidex Moyen',''],['Temps Moyen','Demi-journées']] # Définition du capteur
liste_cap = []
for l in range(6) : 
    liste_cap.append([['Bruits ','dB'],['Température ','°C'],['Humidité ','%'],['Luminosité ','Lux'],['CO2 ','ppm'],['Indice Humidex ',''],['Temps ','Demi-journées']])
liste_cap.append(cap_moy)
# liste_cap sous la forme [cap1,cap2,cap3,cap4,cap5,cap6,cap_moy]
liste_color = ['lime', 'navy', 'crimson', 'darkred', 'dimgray','saddlebrown','darkorange']
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
cap_date = []
tps_moy = []

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
liste_etude_cap = []
liste_etude_donnee = []
cap_date_inter = []

sys.argv =['Projet_Julien_Brian_Groupe_B_V11.py','displayStat',"Température"]

def start():
    if sys.argv[1] == 'display' :
        graph()
    elif sys.argv[1] == 'displayStat' :
        ind_donnee = indice_variable(sys.argv[2])
        tab=[["Numéro du capteur","Moyenne","Variance","Ecart-type","Minimum","Médiane","Maximum","Etendue"]]
        for idd in range(6):
            tab.append([str(idd+1),str(moyenne(liste_cap[idd][ind_donnee][2])),str(variance(liste_cap[idd][ind_donnee][2])),str(ecart_type(liste_cap[idd][ind_donnee][2])),str(minimum(liste_cap[idd][ind_donnee][2])[0]),str(mediane(liste_cap[idd][ind_donnee][2])),str(maximum(liste_cap[idd][ind_donnee][2])[0]),str(etendue(liste_cap[idd][ind_donnee][2]))])
        form="{0:20}{1:10}{2:10}{3:12}{4:10}{5:10}{6:10}{7:10}"
        for val in tab:
            print(form.format(*val))
    elif sys.argv[1] == 'corrélation' :
        print()
    elif sys.argv[1] == 'autre' :
        print()

nb_cap = int(input("Entrez le nombre de capteur à étudier (entre 1 et 6). Attention l'indice de corrélation n'est disponible que pour deux capteurs : "))
if nb_cap == 2 :
    corr = input("Voulez vous afficher l'indice de corrélation des données que vous allez choisir ? (Oui ou Non) ")
    bol_corr = ( 'Oui' == corr )
if nb_cap == 6 :
    for i in range(6) : 
        liste_etude_cap.append(i)
else :
    for i in range(nb_cap) :
        liste_etude_cap.append(int(input("Quel capteur souhaitez vous étudier ? (Entre 1 et 6, un différent à chaque fois) Le capteur : "))-1)
nb_donnee = int(input("Entrez le nombre de donnée à étudier (entre 1 et 6) : "))
if nb_donnee != 6 : 
    for j in range(nb_donnee) :
        liste_etude_donnee.append(int(input("Quelle donnée souhaitez vous étudier ? Donnez le chiffre correspondant : Bruit = 1, Température = 2, Humidité = 3, Luminosité = 4, CO2 = 5, Humidex = 6. "))-1)
else : 
    for j in range(nb_donnee) :
        liste_etude_donnee.append(j)
intervalle = input("Voulez vous étudier cela sur un intervalle donné ? (Oui ou Non) : ")
bol_intervalle = ( 'Oui' == intervalle )
if bol_intervalle :
    date1,date2 = input("Entrez les dates de début et de fin sous la forme : AAAA-MM-JJ HH:MM:SS. Date de début : "),input("Date de fin : ")
tps_occupation = input("Voulez vous étudiez cela pendant les périodes d'occupations des bureaux ? (Oui ou Non) ")
bol_tps_occupation = ( 'Oui' == tps_occupation )
init_moy = input("Voulez vous afficher la courbe moyenne pour les graphiques choisis ? (Oui ou Non) ")
bol_init_moy = ( 'Oui' == init_moy )
# stats = input("Voulez vous afficher les valeurs statistiques ? (Oui ou Non) ")
# bol_stats = ('Oui' == stats)
if nb_donnee != 1 :
    diff = input("Pour finir, voulez vous afficher ces courbes dans des graphiques différents ? (Oui ou Non) ")
    bol_diff = (diff == 'Oui')
else :
    bol_diff = False
    
""" Fonction pour définir la période d'étude """

def occupation(L,cap):
    # print('start')
    if bol_intervalle :
        date_occupation = cap_date_inter.copy()
    else :
        date_occupation = cap_date.copy()
    intervalle_occupation = []
    count_int = 0
    for i in range(len(date_occupation[cap])-1) :
        # print('boucle1')
        if (i > 0 and liste_cap[cap][0][2][i-1] <= 30 and liste_cap[cap][0][2][i] > 30)  or (i == 0 and liste_cap[cap][0][2][i] > 30 and liste_cap[cap][0][2][i+1] > 30):
            # print('yes')
            intervalle_occupation.append([])
            intervalle_occupation[count_int].append(date_occupation[cap][i])
            count_int += 1
        elif i > 0 and liste_cap[cap][0][2][i-1] > 30 and liste_cap[cap][0][2][i] <= 30 :
            # print('no')
            print('i : ', i)
            intervalle_occupation[count_int-1].append(date_occupation[cap][i-1])
    return(intervalle_occupation)

                
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

def liste_intervalle() : # Renvoie une liste identique à liste capte mais seulement avec les données de l'intervale.
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
        cap_date_inter.append([])
        cap_date_inter[-1].append(cap_date[i_debut:i_fin])
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


# Tri fusion nécessaire aux analyses statistiques et autre tri

def fusion(T1,T2) :
    if T1==[] :
        return T2
    if T2==[] :
        return T1
    if T1[0]<T2[0] :
        return [T1[0]]+fusion(T1[1 :],T2)
    else :
        return [T2[0]]+fusion(T1,T2[1 :])

def trifusion(T) : # Tri en ordre croissant
    if len(T)<=1 : 
        return T
    T1=[T[x] for x in range(len(T)//2)]
    T2=[T[x] for x in range(len(T)//2,len(T))]
    return fusion(trifusion(T1),trifusion(T2))

def pop_None(T): # Retire les None d'une liste 
    liste = []
    for element in T :
        if element != None :
            liste.append(element)
    return(liste)

def tri(T): # Tri une liste afin d'analyser correctement les données
    liste = pop_None(T)
    return(trifusion(liste))

# CONVERSION DES LIGNES EN LISTE ET CONVERSION TEMPORELLE
def indice_variable (mot):
    if mot == "Bruit":
        return 0
    elif mot == "Température":
        return 1
    elif mot == "Humidité":
        return 2
    elif mot == "Luminosité":
        return 3
    elif mot == "CO2":
        return 4 
    elif mot == "Humidex":
        return 5
    else : 
        raise NameError ("Veuillez chosir entre c'est 6 variable: Bruit, Température, Humidité, Luminosité, CO2, Humidex")

def saut_first_col(l) : # Prend en argument une chaîne de caractère composée d'un ';'
    m = 0
    car = l[m]
    while car != ';' :
        m += 1
        car = l[m]
    return(l[m+1:]) # Elle renvoie tout ce qui est après ce point virgule, pour supprimer la colonne "id"
            
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

# ANALYSE STATISTIQUE DES DONNEES

def maximum(liste): # Les listes utilisées contiennent soit des nombres, soit des couples de nombre
    ind_max = 0
    maxi = 0 
    # print(liste)
    if type(liste[0]) == list :
        for element in liste :
            # print(element,'ys')
            if element[0] != None :
                if maxi < element[0] :
                    ind_max = element[1]
                    maxi = element[0]
    else :
        for a in range(len(liste)):
            if liste[a] != None :
                if maxi < liste[a] :
                    ind_max = a
                    maxi = liste[a]
    # print([maxi,ind_max])
    return [int(maxi*10000/10000),ind_max]

def minimum(liste):
    ind_min = 0
    mini = 10000
    if type(liste[0]) == list :
        for element in liste :
            if element[0] != None :
                if mini > element[0] :
                    ind_min = element[1]
                    mini = element[0]
    else :
        for i in range(len(liste)):
            if liste[i] != None:
                if mini > liste[i]:
                    ind_min = i
                    mini = liste[i]
    return [int(mini*10000)/10000,ind_min]

def mediane(liste):
    n = len(liste)
    if n%2==0:
        return (int(((liste[(n//2)-1] + liste[n//2])/2)*10000)/10000)
    else :
        return (int(liste[(n//2)]*10000)/10000)
    
def count_None(liste):
    count_n = 0
    for element in liste :
        if element == None :
            count_n += 1
    return (int(count_n*10000)/10000)

def somme(liste,bol):
    somme1,somme2 = 0,0
    for element in liste:
        if element != None :
            somme1 += element 
            somme2 += element ** 2
    if bol==True:
        return (int(somme1*10000)/10000)
    else:
        return (int(somme2*10000)/10000)

def moyenne(liste):
    addition = somme(liste,True)
    return (int((addition/(len(liste)-count_None(liste)))*10000)/10000)

def etendue(liste):
    maxi = maximum(liste)[0]
    mini = minimum(liste)[0]
    return (int((maxi-mini)*10000)/10000)

def variance(liste):
    moy = moyenne(liste)
    addition = somme(liste,False)
    return (int((addition/(len(liste)-count_None(liste)) - moy**2)*10000)/10000)

def ecart_type(liste):
    return (int(variance(liste)**(1/2)*10000)/10000)      

def covariance(L1,L2):
    if count_None(L1) > 0 or count_None(L2)>0 :
        return("Prendre un autre intervalle de temps")
    moy1= moyenne(L1)
    moy2= moyenne(L2)
    S=0
    for i in range(len(L1)):
        S += (L1[i]-moy1)*(L2[i]-moy2)
    return (int(S/len(L1)*10000)/10000)

def indice_correlation(L1,L2):
    if len(L1)!=len(L2) :
        return("Prendre un autre intervalle de temps")
    indice = covariance(L1,L2)/(ecart_type(L1)*ecart_type(L2))
    return (int(indice*10000)/10000)

# ANALYSE PHYSIQUE 

a = 17.27
b = 237.7

def alpha(T,phi):
    return(a * T / (b+T) + mt.log(phi))

def humidex(T,phi) :
    temp_rosee = (phi/100)**(1/8)*(112 + 0.9 * T) + 0.1 * T - 112
    return( T + 0.5555 * (6.11 * mt.exp(5417.7530 * (1 / 273.16 - 1 / (273.15 + temp_rosee))) - 10))

# Graphique

def fusion_str(string,nombre):
    return(string + ' : ' + str(int(nombre*10000)/10000))

def titre(bol_tous,cap,donnee) :
    titre = "Relevé capteur "
    if bol_tous :
        count = 0
        for i in liste_etude_cap:
            if count != n:
                titre = titre + str(i + 1) + ", "
            else:
                titre = titre + str(i+1) + " : "
            count += 1
        titre = titre + str(liste_cap[0][donnee][0]) + " :"
    else :
        if cap == 'Moyen' :
            titre = titre + cap + " : " + liste_cap[-1][donnee][0] + " :"
        else :
            titre = titre + str(cap+1) + " : " + liste_cap[cap][donnee][0] + " :"
    return(titre)
        
def lab(bol_tous,donnee):
    lab = liste_cap[0][donnee][1]
    return lab

def graph() :
    if bol_intervalle :
        liste_int = liste_intervalle()
        # print(liste_int)
        for id_donnee in liste_etude_donnee : 
            liste_max = []
            liste_min = []
            if nb_cap == 2 :
                if bol_corr :
                    ind_corr = indice_correlation(liste_int[liste_etude_cap[0]][id_donnee][2],liste_int[liste_etude_cap[1]][id_donnee][2])
            for idd in liste_etude_cap :
                plt.plot(liste_int[idd][-1][2],liste_int[idd][id_donnee][2], color = liste_color[idd], label = liste_int[idd][id_donnee][0] + " " + str(idd+1))
                M = maximum(liste_int[idd][id_donnee][2])
                m = minimum(liste_int[idd][id_donnee][2])
                liste_max.append(M)
                liste_min.append(m)
                if bol_diff :
                    plt.title(titre(False,idd,id_donnee))
                    plt.ylabel(lab(False,id_donnee))
                    plt.legend(loc='upper right')
                    plt.xlim(0,40)
                    plt.xlabel('Temps en demi-journée')
                    plt.annotate(fusion_str('Maximum',liste_max[-1][0]), xy = (liste_max[-1][1]*15/60/12, liste_max[-1][0]), xytext = (30, liste_max[-1][0]*0.7+5),
                                 arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'red')
                    plt.annotate(fusion_str('Minimum',liste_min[-1][0]), xy = (liste_min[-1][1]*15/60/12, liste_min[-1][0]), xytext = (30, liste_min[-1][0]*1.3-5),
                                 arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'blue')                    
                    plt.show()
            if bol_init_moy :
                plt.plot(liste_int[-1][-1][2],liste_int[-1][id_donnee][2], color = liste_color[-1], label = liste_int[-1][id_donnee][0])
                maxi_moy = maximum(liste_int[-1][id_donnee][2])
                mini_moy = minimum(liste_int[-1][id_donnee][2])
                maxi = maximum(liste_max + [maxi_moy])
                mini = minimum(liste_min + [mini_moy])
                if bol_diff :
                    plt.title(titre(False,'Moyen',id_donnee))
                    plt.ylabel(lab(False,id_donnee))
                    plt.legend(loc='upper right')
                    plt.xlim(0,40)
                    plt.xlabel('Temps en demi-journée')
                    plt.annotate(fusion_str('Maximum',maxi_moy[0]), xy = (maxi_moy[1]*15/60/12, maxi_moy[0]), xytext = (30, maxi_moy[0]*0.7+5),
                                 arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'red')
                    plt.annotate(fusion_str('Minimum',mini_moy[0]), xy = (mini_moy[1]*15/60/12, mini_moy[0]), xytext = (30, mini_moy[0]*1.3-5),
                                 arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'blue')
                    plt.show()
            if bol_diff == False :
                plt.title(titre(True,0,id_donnee))
                plt.ylabel(lab(True,id_donnee))
                plt.legend(loc='upper right')
                plt.xlim(0,40)
                plt.xlabel('Temps en demi-journée')
                if bol_init_moy == False :
                    maxi = maximum(liste_max)
                    mini = minimum(liste_min)
                plt.annotate(fusion_str('Maximum',maxi[0]), xy = (maxi[1]*15/60/12, maxi[0]), xytext = (30, maxi[0]*0.43+10),
                             arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'red')
                plt.annotate(fusion_str('Minimum',mini[0]), xy = (mini[1]*15/60/12, mini[0]), xytext = (30, mini[0]*1.2-5),
                             arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'blue')
                if nb_cap == 2 : 
                    if bol_corr :
                        if type(ind_corr) == float :
                            if donnee == 3 :
                                plt.text(29,100, "Indice de corrélation : ")
                                plt.text(29,liste_min[idd], ind_corr)
                            else :
                                plt.text(29 ,liste_min[idd]*1.08, "Indice de corrélation : ")
                                plt.text(29,liste_min[idd], ind_corr)
                plt.show()
    else :
        for id_donnee in liste_etude_donnee :
            liste_max = []
            liste_min = []
            if nb_cap == 2 :
                if bol_corr :
                    ind_corr = indice_correlation(liste_cap[liste_etude_cap[0]][id_donnee][2],liste_cap[liste_etude_cap[1]][id_donnee][2])
            for idd in liste_etude_cap :
                plt.plot(liste_cap[idd][-1][2],liste_cap[idd][id_donnee][2], color = liste_color[idd], label = liste_cap[idd][id_donnee][0] + " " + str(idd+1))
                M = maximum(liste_cap[idd][id_donnee][2])
                m = minimum(liste_cap[idd][id_donnee][2])
                liste_max.append(M)
                liste_min.append(m)
                if bol_diff :
                    plt.title(titre(False,idd,id_donnee))
                    plt.ylabel(lab(False,id_donnee))
                    plt.legend(loc='upper right')
                    plt.xlim(0,40)
                    plt.xlabel('Temps en demi-journée')
                    plt.annotate(fusion_str('Maximum',liste_max[-1][0]), xy = (liste_max[-1][1]*15/60/12, liste_max[-1][0]), xytext = (30, liste_max[-1][0]*0.7+5),
                                 arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'red')
                    plt.annotate(fusion_str('Minimum',liste_min[-1][0]), xy = (liste_min[-1][1]*15/60/12, liste_min[-1][0]), xytext = (30, liste_min[-1][0]*1.3-5),
                                 arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'blue')                    
                    plt.show()
            if bol_init_moy :
                plt.plot(liste_cap[-1][-1][2],liste_cap[-1][id_donnee][2], color = liste_color[-1], label = liste_cap[-1][id_donnee][0])
                maxi_moy = maximum(liste_cap[-1][id_donnee][2])
                mini_moy = minimum(liste_cap[-1][id_donnee][2])
                maxi = maximum(liste_max + [maxi_moy])
                mini = minimum(liste_min + [mini_moy])
                if bol_diff :
                    plt.title(titre(False,'Moyen',id_donnee))
                    plt.ylabel(lab(False,id_donnee))
                    plt.legend(loc='upper right')
                    plt.xlim(0,40)
                    plt.xlabel('Temps en demi-journée')
                    plt.annotate(fusion_str('Maximum',maxi_moy[0]), xy = (maxi_moy[1]*15/60/12, maxi_moy[0]), xytext = (30, maxi_moy[0]*0.7+5),
                                 arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'red')
                    plt.annotate(fusion_str('Minimum',mini_moy[0]), xy = (mini_moy[1]*15/60/12, mini_moy[0]), xytext = (30, mini_moy[0]*1.3-5),
                                 arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                                'width': 3, 'headwidth': 15,
                                'shrink': 0.05}, color = 'blue')
                    plt.show()
            if bol_diff == False :
                plt.title(titre(True,0,id_donnee))
                plt.ylabel(lab(True,id_donnee))
                plt.legend(loc='upper right')
                plt.xlim(0,40)
                plt.xlabel('Temps en demi-journée')
                if bol_init_moy == False :
                    maxi = maximum(liste_max)
                    mini = minimum(liste_min)
                plt.annotate(fusion_str('Maximum',maxi[0]), xy = (maxi[1]*15/60/12, maxi[0]), xytext = (30, maxi[0]*0.43+10),
                             arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'red')
                plt.annotate(fusion_str('Minimum',mini[0]), xy = (mini[1]*15/60/12, mini[0]), xytext = (30, mini[0]*1.3-5),
                             arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'blue')
                if nb_cap == 2 : 
                    if bol_corr :
                        if type(ind_corr) == float :
                            if donnee == 3 :
                                plt.text(29,100, "Indice de corrélation : ")
                                plt.text(29,liste_min[idd], ind_corr)
                            else :
                                plt.text(29 ,liste_min[idd]*1.08, "Indice de corrélation : ")
                                plt.text(29,liste_min[idd], ind_corr)
                plt.show()

""" Enregistrement des données dans les listes en vue de faire apparaître les différentes données et diagrammes """

with open("EIVP_KM correction.csv","r") as mesures : # Ouverture du fichier csv
    mesures.readline() # Saut de la première ligne
    ligne = saut_first_col(mesures.readline()) # Affectation de la première ligne
    i = 2 # Initialisation du compteur de ligne
    bol_enregistrement = True # bol_enregistrement sert à savoir si l'on ajoute les données dans nos listes ou non (pour palier au problème du trou dans le capteur 5 notamment)
    count = 0 
    count_min = 10000
    while i != 7883 : # Il y a bien 7882 lignes mais on a besoin de retourner une dernière fois dans la boucle pour afficher les dernière courbes.
        if 984 <= count < 1164 and idd == 5 :
            bol_enregistrement = False
        else :
            bol_enregistrement = True
        if int(ligne[0]) == idd and bol_enregistrement == True : # Tant que l'id du capteur est bon, on affecte aux listes les valeurs correspondantes 
            i += 1
            bruits.append(float(ligne[2:6]))
            temp.append(float(ligne[7:11]))
            humidity.append(float(ligne[12:16]))
            ind_humidex.append(humidex(temp[-1],humidity[-1]))
            k = 52 - len(ligne)
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
        elif int(ligne[0]) == idd and bol_enregistrement == False :
            count += 1
        elif int(ligne[0]) != idd :
            date_init = '2019-08-11 11:30:50' # Date d'allumage du premier capteur (le numéro 5)
            tps = []
            cap_date.append(date)
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
        nb_none = 0
        for j in range(6) : # Tourne dans les capteurs
            if liste_cap[j][i][2][p] == None :
                nb_none += 1
        liste_donnee_moy[i].append(liste_somme_moy[i][p] / (6-nb_none))
    p += 1

tps_moy = tps.copy()
liste_donnee_moy.append(tps_moy)
for k in range (len(liste_donnee_moy)) :
    liste_cap[-1][k].append(liste_donnee_moy[k])

# print(etendue(liste_cap[0][0][2]))
# print(indice_correlation(liste_cap[5][0][2], liste_cap[1][0][2]))

# graph()
start()