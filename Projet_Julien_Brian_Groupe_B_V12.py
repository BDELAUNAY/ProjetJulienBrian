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
""" Fusionner graph int et cap (check)"""
""" Tableau des valeurs (check)"""
""" Assurer la continuité avec les ordres possibles (check)"""
""" EN GROS FAIRE LA FONCTION START() et c'est fini !!!!!!!!!! (check)"""
""" Mettre des None si l'intervalle prend dans les mauvais temps (check)"""
""" Graph occupation (check)"""
""" ERREURS A METTRE (check)"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def start():
    n = len(sys.argv)
    print('\n')
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('\n')
    if n == 1 :
        info = input("Bonjour, voulez vous affichez les informations nécessaires à l'utilisation du programme ? Si oui entrez n'importe quel caractère, sinon appuyez sur le bouton Entrée : ")
        bol_info = (info != '')
    else :
        bol_info = False
    if bol_info : 
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print('\n',"Chers examinateurs, bienvenue sur le Projet python de Julien et Brian",'\n') 
        print(" *** Les commandes à utiliser en premier argument sont les suivantes : ",'\n', " - <display> <variable> (<date_debut> <date_fin>) : Permet d'afficher le graphique d'une variable pour les six capteurs",'\n', " - <displayStat> <variable> (<date_debut> <date_fin>) : Affiche un tableau des différentes données statistisques d'une variable pour les six capteurs",'\n', " - <corrélation> <variable1> <variable2> (<date_debut> <date_fin>) : Affiche les deux variables sur un même graphique pour chaque capteur, avec l'indice de corrélation correspondant",'\n'," - <autre> (<date_debut> <date_fin>) : Permet d'afficher le nombre de capteur que vous souhaitez ainsi que le nombre de variable à traiter, en vous laissant le choix sur les propriétés du graphique,",'\n'," essayez tout ce que vous souhaitez ! ", '\n', " - <occupation> (<date_debut> <date_fin>) : Affiche le graphique représentant les périodes d'occupation du bureau",'\n','\n', "Attention cependant : les dates sont optionnelles mais les deux bornes sont nécessaires si vous souhaitez les utiliser,",'\n',"de plus si vous souhaitez afficher les données dans un intervalle de temps qui n'a pa été mesuré par les capteurs, les graphiques seront logiquement blanc, vous devrez alors recommencer avec de nouvelles dates",'\n')
        print(" *** Les différentes variables sont : Bruit, Température, Humidité, Luminosité, CO2, Humidex",'\n')
        print(" *** Si vous rencontrez des problèmes avec les dates sachez qu'ils faut les écrire sous format : AAAA-MM-JJ",'\n', "Ces dates s'étendent du 2019-08-11 au 2019-08-25",'\n')
        return()
    liste_etude_cap = []
    liste_etude_donnee = []
    cap_date_inter = []
    if n == 1 :
        return ()
    if sys.argv[1] == 'display' :
        for i in range(6) : 
            liste_etude_cap.append(i)
        liste_etude_donnee.append(indice_variable(sys.argv[2]))
        if n > 3:
            erreur_date(sys.argv[3],sys.argv[4])
            bol_intervalle = True
            date1,date2 = sys.argv[3]+' 00:00:00',sys.argv[4]+' 00:00:00'
        else :
            bol_intervalle = False
            date1,date2 = '',''
        graph(6,False,1,bol_intervalle,date1,date2,True,False,False,liste_etude_cap,liste_etude_donnee,cap_date_inter)
    elif sys.argv[1] == 'displayStat' :
        if n > 3:
            erreur_date(sys.argv[3],sys.argv[4])
            bol_intervalle = True
            date1,date2 = sys.argv[3]+' 00:00:00',sys.argv[4]+' 00:00:00'
        else :
            bol_intervalle = False
            date1,date2 = '',''
        id_donnee = indice_variable(sys.argv[2])
        tab=[["Numéro du capteur","Moyenne","Variance","Ecart-type","Minimum","Médiane","Maximum","Etendue"]]
        print(liste_cap[0][id_donnee][0] + ' : ')
        for idd in range(6):
            tab.append([str(idd+1),str(moyenne(liste_cap[idd][id_donnee][2])),str(variance(liste_cap[idd][id_donnee][2])),str(ecart_type(liste_cap[idd][id_donnee][2])),str(minimum(liste_cap[idd][id_donnee][2])[0]),str(mediane(liste_cap[idd][id_donnee][2])),str(maximum(liste_cap[idd][id_donnee][2])[0]),str(etendue(liste_cap[idd][id_donnee][2]))])
        form="{0:20}{1:10}{2:12}{3:12}{4:10}{5:10}{6:10}{7:10}"
        for val in tab:
            print(form.format(*val))
    elif sys.argv[1] == 'corrélation' :
        liste_etude_donnee = [indice_variable(sys.argv[2]),indice_variable(sys.argv[3])]
        print(liste_etude_donnee)
        if n > 4 :
            erreur_date(sys.argv[4],sys.argv[5])
            bol_intervalle = True
            date1,date2 = sys.argv[4]+' 00:00:00',sys.argv[5]+' 00:00:00'
        else :
            bol_intervalle = False
            date1,date2 = '',''
        print('yes')
        graph_corr(6,True,2,bol_intervalle,date1,date2,False,False,True,[0,1,2,3,4,5],liste_etude_donnee,cap_date_inter)
    elif sys.argv[1] == 'autre' :
        if n > 2 :
            erreur_date(sys.argv[2],sys.argv[3])
            bol_intervalle = True
            date1,date2 = sys.argv[2]+' 00:00:00',sys.argv[3]+' 00:00:00'
        else :
            bol_intervalle = False
            date1,date2 = '',''
        nb_cap = int(input("Entrez le nombre de capteur à étudier (entre 1 et 6). Attention l'indice de corrélation n'est disponible que pour deux capteurs : "))
        if nb_cap == 2 :
            corr = input("Voulez vous afficher l'indice de corrélation des données que vous allez choisir ? (Oui ou Non) ")
            bol_corr = ( 'Oui' == corr )
        else :
            bol_corr = False
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
        init_moy = input("Voulez vous afficher la courbe moyenne pour les graphiques choisis ? (Oui ou Non) ")
        bol_init_moy = ( 'Oui' == init_moy )
        stats = input("Voulez vous afficher les valeurs statistiques ? (Oui ou Non) ")
        bol_stats = ('Oui' == stats)
        if nb_donnee != 1 :
            diff = input("Pour finir, voulez vous afficher ces courbes dans des graphiques différents ? (Oui ou Non) ")
            bol_diff = (diff == 'Oui')
        else :
            bol_diff = False
        if bol_stats :
            for id_donnee in liste_etude_donnee :
                print(liste_cap[0][id_donnee][0] + ' : ')
                tab=[["Numéro du capteur","Moyenne","Variance","Ecart-type","Minimum","Médiane","Maximum","Etendue"]]
                for idd in range(6):
                    tab.append([str(idd+1),str(moyenne(liste_cap[idd][id_donnee][2])),str(variance(liste_cap[idd][id_donnee][2])),str(ecart_type(liste_cap[idd][id_donnee][2])),str(minimum(liste_cap[idd][id_donnee][2])[0]),str(mediane(liste_cap[idd][id_donnee][2])),str(maximum(liste_cap[idd][id_donnee][2])[0]),str(etendue(liste_cap[idd][id_donnee][2]))])
                form="{0:20}{1:10}{2:12}{3:12}{4:10}{5:10}{6:10}{7:10}"
                for val in tab:
                    print(form.format(*val))
        graph(nb_cap,bol_corr,nb_donnee,bol_intervalle,date1,date2,bol_init_moy,bol_stats,bol_diff,liste_etude_cap,liste_etude_donnee,cap_date_inter)
    elif sys.argv[1] == 'occupation' :
        tps = input("Voulez-vous affichez le temps en date (1) ou en demi_journées (2), sachant que le chargement sera plus long pour les dates ? Entrez le chiffre correspondant au choix : ")
        bol_tps = (tps == '1')
        if n > 2 :
            erreur_date(sys.argv[2],sys.argv[3])
            bol_intervalle = True
            date1,date2 = sys.argv[2]+' 00:00:00',sys.argv[3]+' 00:00:00'
        else :
            bol_intervalle = False
            date1,date2 = '',''
        occup = occupation(bol_intervalle, date1, date2,bol_tps)
        plt.plot(occup[0],occup[1],label = 'Occupation : ' + '\n' + '1 pour Occupé' + '\n' + '0 pour Inoccupé')
        if bol_tps :
            plt.xlabel = ('Dates')
        else :
            plt.xlim(0,45)
        plt.legend()
        plt.title("Périodes d'occupation des bureaux")

        plt.show()

""" Fonction pour définir la période d'étude """

def occupation(bol_intervalle,date1,date2,bol_tps):
    if bol_intervalle :
        liste_date = date_intervalle(date1,date2)
        liste = liste_intervalle(date1, date2, [0,1,2,3,4,5], [0,1,2,3,4,5], liste_date, False).copy()
    else :
        liste_date = cap_date[5].copy()
        liste = liste_cap.copy()
    occup = [[],[]]
    for i in range(len(liste_date)):
        if bol_tps :
            occup[0].append(liste_date[i][0])
        else :
            occup[0].append(liste[6][-1][2][i])
        if i != len(liste_date)-1 and i != 0 :
            if liste[6][0][2][i] <= 35.5 and (liste[6][0][2][i+1] < 35.5 or liste[6][0][2][i-1] < 35.5) :
                occup[1].append(0)
            else :
                occup[1].append(1)
        else :
            if liste[6][0][2][i] <= 35.5 :
                occup[1].append(0)
            else :
                occup[1].append(1)
    return(occup)            

def indices_intervalle(date1,date2) : # Identifie les indices correspondant à l'intervalle demandé
    tps_debut,tps_fin = distance_temporelle(date1)/3600/12,distance_temporelle(date2)/3600/12
    i_debut = 0
    while liste_cap[5][-1][2][i_debut] < tps_debut :
        i_debut += 1
    i_fin = i_debut
    while liste_cap[5][-1][2][i_fin] < tps_fin :
        i_fin += 1
    return(i_debut,i_fin)

def liste_intervalle(date1,date2,liste_etude_cap,liste_etude_donnee,cap_date_inter,bol_init_moy) : # Renvoie une liste identique à liste capte mais seulement avec les données de l'intervale.
    liste = []
    i_debut,i_fin = indices_intervalle(date1,date2)
    i = 0 # i va aller de 0 à nb_cap-1 (indice pour liste, tandis que cap est l'indice pour liste_cap)
    for cap in [0,1,2,3,4,5] : 
        liste.append([])
        j = 0 # j va aller de 0 à nb_donnee-1 (indice pour liste[i], tandis que donnee est l'indice pour liste_cap[cap])
        for donnee in [0,1,2,3,4,5] :
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
        for donnee in [0,1,2,3,4,5] :
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

def date_intervalle(date1,date2) :
    cap_date_inter = []
    i_debut,i_fin = indices_intervalle(date1,date2)
    for i in len(cap_date[i_debut:i_fin]):
        cap_date_inter.append([cap_date[i],i])
    return(cap_date_inter)

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
    for id in range(6):
        if mot == liste_cap[0][id][0] :
            return id
    else : 
        raise NameError ("Veuillez chosir entre ces 6 variables  : Bruit, Température, Humidité, Luminosité, CO2, Humidex")

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
    return (int((variance(liste)**(1/2))*10000)/10000)      

def covariance(L1,L2):
    T1 = []
    T2 = []
    for i in range(len(L1)) :
        if L1[i] != None and L2[i] != None :
            T1.append(L1[i])
            T2.append(L2[i])
    moy1= moyenne(T1)
    moy2= moyenne(T2)
    S=0
    for i in range(len(T1)):
        S += (T1[i]-moy1)*(T2[i]-moy2)
    return (int(S/len(T1)*10000)/10000)

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

def titre(bol_tous,cap,donnee,liste_etude_cap) :
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

def graph(nb_cap,bol_corr,nb_donnee,bol_intervalle,date1,date2,bol_init_moy,bol_stats,bol_diff,liste_etude_cap,liste_etude_donnee,cap_date_inter) :
    if bol_intervalle :
        liste=liste_intervalle(date1,date2,liste_etude_cap,liste_etude_donnee,cap_date_inter,bol_init_moy).copy()
    else :
        liste=liste_cap.copy()
    for id_donnee in liste_etude_donnee : 
        liste_max = []
        liste_min = []
        if nb_cap == 2 :
            if bol_corr :
                ind_corr = indice_correlation(liste[liste_etude_cap[0]][id_donnee][2],liste[liste_etude_cap[1]][id_donnee][2])
        for idd in liste_etude_cap :
            plt.plot(liste[idd][-1][2],liste[idd][id_donnee][2], color = liste_color[idd], label = liste[idd][id_donnee][0] + " " + str(idd+1))
            M = maximum(liste[idd][id_donnee][2])
            m = minimum(liste[idd][id_donnee][2])
            liste_max.append(M)
            liste_min.append(m)
            if bol_diff :
                plt.title(titre(False,idd,id_donnee,liste_etude_cap))
                plt.ylabel(lab(False,id_donnee))
                plt.legend(loc='upper right')
                plt.xlim(0,40)
                plt.xlabel('Temps en demi-journée')
                plt.annotate(fusion_str('Maximum',liste_max[-1][0]), xy = (liste_max[-1][1]*15/60/12, liste_max[-1][0]), xytext = (40, liste_max[-1][0]/1.5),
                             arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'red')
                plt.annotate(fusion_str('Minimum',liste_min[-1][0]), xy = (liste_min[-1][1]*15/60/12, liste_min[-1][0]), xytext = (30, liste_max[-1][0]/1.5),
                             arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'blue')                    
                plt.show()
        if bol_init_moy :
            plt.plot(liste[-1][-1][2],liste[-1][id_donnee][2], color = liste_color[-1], label = liste[-1][id_donnee][0])
            maxi_moy = maximum(liste[-1][id_donnee][2])
            mini_moy = minimum(liste[-1][id_donnee][2])
            maxi = maximum(liste_max + [maxi_moy])
            mini = minimum(liste_min + [mini_moy])
            if bol_diff :
                plt.title(titre(False,'Moyen',id_donnee,liste_etude_cap))
                plt.ylabel(lab(False,id_donnee))
                plt.legend(loc='upper right')
                plt.xlim(0,40)
                plt.xlabel('Temps en demi-journée')
                plt.annotate(fusion_str('Maximum',maxi_moy[0]), xy = (maxi_moy[1]*15/60/12, maxi_moy[0]), xytext = (40, maxi_moy[0]/1.5),
                             arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'red')
                plt.annotate(fusion_str('Minimum',mini_moy[0]), xy = (mini_moy[1]*15/60/12, mini_moy[0]), xytext = (30, maxi_moy[0]/1.5),
                             arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                            'width': 3, 'headwidth': 15,
                            'shrink': 0.05}, color = 'blue')
                plt.show()
        if bol_diff == False :
            plt.title(titre(True,0,id_donnee,liste_etude_cap))
            plt.ylabel(lab(True,id_donnee))
            plt.legend(loc='upper right')
            plt.xlim(0,40)
            plt.xlabel('Temps en demi-journée')
            if bol_init_moy == False :
                maxi = maximum(liste_max)
                mini = minimum(liste_min)
            plt.annotate(fusion_str('Maximum',maxi[0]), xy = (maxi[1]*15/60/12, maxi[0]), xytext = (40, maxi[0]/1.5),
                         arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                        'width': 3, 'headwidth': 15,
                        'shrink': 0.05}, color = 'red')
            plt.annotate(fusion_str('Minimum',mini[0]), xy = (mini[1]*15/60/12, mini[0]), xytext = (30, maxi[0]/1.5),
                         arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                        'width': 3, 'headwidth': 15,
                        'shrink': 0.05}, color = 'blue')
            if nb_cap == 2 : 
                if bol_corr :
                    plt.legend(loc='upper right',title = 'Indice de Corrélation : ' + '\n' + str(ind_corr))
            plt.show()

def graph_corr(nb_cap,bol_corr,nb_donnee,bol_intervalle,date1,date2,bol_init_moy,bol_stats,bol_diff,liste_etude_cap,liste_etude_donnee,cap_date_inter) :
    if bol_intervalle :
        liste=liste_intervalle(date1,date2,liste_etude_cap,liste_etude_donnee,cap_date_inter,bol_init_moy).copy()
    else :
        liste=liste_cap.copy()
    for cap in liste_etude_cap : 
        liste_max = []
        liste_min = []
        print((liste[cap]))
        ind_corr = indice_correlation(liste[cap][liste_etude_donnee[0]][2],liste[cap][liste_etude_donnee[1]][2])
        for id_donnee in liste_etude_donnee :
            plt.plot(liste[cap][-1][2],liste[cap][id_donnee][2], color = liste_color[id_donnee], label = liste[cap][id_donnee][0] + " " + str(cap+1))
            M = maximum(liste[cap][id_donnee][2])
            m = minimum(liste[cap][id_donnee][2])
            liste_max.append(M)
            liste_min.append(m)
            plt.title(titre(False,cap,liste_etude_donnee[0],liste_etude_cap)+' '+liste[cap][liste_etude_donnee[1]][0]+' :')
            plt.ylabel(lab(False,liste_etude_donnee[0])+' '+lab(False,liste_etude_donnee[1]))
            plt.legend(loc='upper right',title = 'Indice de Corrélation : ' + '\n' + str(ind_corr))
            plt.xlim(0,40)
            plt.xlabel('Temps en demi-journée')
            plt.annotate(fusion_str('Maximum',liste_max[-1][0]), xy = (liste_max[-1][1]*15/60/12, liste_max[-1][0]), xytext = (40, liste_max[-1][0]/1.5),
                         arrowprops = {'facecolor': 'red', 'edgecolor': 'red',
                        'width': 3, 'headwidth': 15,
                        'shrink': 0.05}, color = 'red')
            plt.annotate(fusion_str('Minimum',liste_min[-1][0]), xy = (liste_min[-1][1]*15/60/12, liste_min[-1][0]), xytext = (30, liste_max[-1][0]/1.5),
                         arrowprops = {'facecolor': 'blue', 'edgecolor': 'blue',
                        'width': 3, 'headwidth': 15,
                        'shrink': 0.05}, color = 'blue')
        plt.show()

""" Fonction d'erreurs """

def erreur_date(date1,date2):
    if date1 < '2019-08-11' :
        raise ValueError("Erreur : la date choisie est antérieure à la date de début de fonctionnement du premier capteur : 2019-08-11. Veuillez choisir cette dernière ou une autre date ultérieure.")
    elif date2 > '2019-08-25' :
        raise ValueError("Erreur : la date choisie est ultérieure à la date de fin de fonctionnement du dernier capteur : 2019-08-25. Veuillez choisir cette dernière ou une autre date antérieure.")


""" Définition des premières variables"""

cap_moy = [['Bruit Moyen','dB'],['Température Moyen','°C'],['Humidité Moyenne','%'],['Luminosité Moyenne','Lux'],['CO2 Moyen','ppm'],['Indice Humidex Moyen',''],['Temps Moyen','Demi-journées']] # Définition du capteur
liste_cap = []
for l in range(6) : 
    liste_cap.append([['Bruit','dB'],['Température','°C'],['Humidité','%'],['Luminosité','Lux'],['CO2','ppm'],['Humidex',''],['Temps','Demi-journées']])
liste_cap.append(cap_moy) # liste_cap sous la forme [cap1,cap2,cap3,cap4,cap5,cap6,cap_moy]
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
            lum.append(float(ligne[17:21-k]))
            co2.append(float(ligne[22-k:25-k]))
            date.append([ligne[26-k:45-k],count])
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
                tps.append(distance_temporelle(date[k][0])/3600/12)
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
    

start()