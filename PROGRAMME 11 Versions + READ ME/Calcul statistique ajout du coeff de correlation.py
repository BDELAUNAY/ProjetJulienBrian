# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:27:55 2020

@author: Julien
"""

liste_test = [1,5,9,7,6,8,4,6,9,5,9]
liste_test2= [1,5,6,9,8,4,5,2,3,5,8]


def maximum(liste):
    maxi = 0 
    for element in liste:
        if element != "None":
            if maxi < element:
                maxi = element
    return maxi

print(maximum(liste_test))


def minimum(liste):
    mini = 10000
    for element in liste:
        if element != "None":
            if mini > element:
                mini = element
    return mini

print(minimum(liste_test))


def mediane(liste):
    n = len(liste)
    if n%2==0:
        return (liste[(n//2)-1] + liste[n//2])/2
    else :
        return liste[(n//2)]
    

print(mediane(liste_test))


def somme(liste,bol):
    somme1,somme2 = 0,0
    for element in liste:
        somme1 += element 
        somme2 += element ** 2
    if bol==True:
        return somme1
    else:
        return somme2
    
print(somme(liste_test,True))
print(somme(liste_test,False))

def moyenne(liste):
    addition = somme(liste,True)
    return addition/len(liste)
        
print (moyenne(liste_test))
    
def etendue(liste):
    return maximum(liste)-minimum(liste)

print(etendue(liste_test))



def variance(liste):
    moy = moyenne(liste)
    addition = somme(liste,False)
    return addition/len(liste) - moy**2
    
print(variance(liste_test))


def ecart_type(liste):
    return variance(liste)**(1/2)

print("ecart type" + str(ecart_type(liste_test2)))
        

def covariance(L1,L2):
    if len(L1) == len(L2):
        moy1= moyenne(L1)
        moy2= moyenne(L2)
        S=0
        for i in range(len(L1)):
            S += (L1[i]-moy1)*(L2[i]-moy2)
        return S/len(L1)
    else :
        return "prendre un autre intervalle de temps"

print(covariance(liste_test,liste_test2))

def indice_correlation(L1,L2):
    coef= covariance(L1,L2)/(ecart_type(L1)*ecart_type(L2))
    return (coef)
    
print(indice_correlation(liste_test, liste_test2)) 
    
    

#premiere écriture du programme avant modification par fonction pour le simplifier


# # Calcul du maximum en fonction des capteurs 

#     for i in range (5) : #varie de 0 1 2 3 4 id des données
#         for j in range (6) : #numéro des capteurs
#             print("max du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :" + str(max(liste_cap[j][i][2])))
#             if i==4 and j==5:
#                 print("\n")



# #calcul du minimum e fonction des capteurs
# for i in range (5) :
#     for j in range (6) :
#         print("min du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :" + str(min(liste_cap[j][i][2])))
#         if i==4 and j==5:
#             print ("\n")
#             #str() transforme un chiffre en chaîne
            



# #calcul de la médiane
# for i in range (5) :
#     for j in range (6) :
#         print("médiane du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " :" + str(len(liste_cap[j][i][2])/2))
#         if i==4 and j==5:
#             print ("\n")




# #calcul de la moyenne des différent capteur
# def moyenne () :
#     for i in range (5) :
#         for j in range (6) :
#             somme=0
#             for element in liste_cap[j][i][2]:
#                 somme += element
#             print("moyenne du capteur " + liste_cap[j][i][0] + " " + str(j+1) + " : " + str(somme/len(liste_cap[j][i][2]))[:6])
            
# moyenne()
# print("\n")




# # Calcul de L'étendue
# for i in range (5) :
#     for j in range (6) :
#         print("etendue du capteur" + liste_cap[j][i][0] + " " + str(j+1) + " : " + str(max(liste_cap[j][i][2])-min(liste_cap[j][i][2]))[:6])
#         if i==4 and j==5:
#             print("\n")
            

    
# x = int(input("quelle mesures desirez vous? : "))
# # Definition des numéros:
# Bruit = 1
# Temperature = 2
# Humidite = 3
# Luminosite = 4
# CO2 = 5

# if x == 1: 
#     for i in range (6):
#         print("\n" + "max du capteur " + liste_cap[i][x-1][0] + " " + str(i+1) + " :" + str(max(liste_cap[i][x-1][2])) 
#               + "\n" + "min du capteur " + liste_cap[i][x-1][0] + " " + str(i+1) + " :" + str(min(liste_cap[i][x-1][2]))
              
#               + "\n" + "médiane du capteur " + liste_cap[x-1][i][0] + " " + str(i+1) + " : " + str(len(liste_cap[i][x-1][2])/2)
              
#               + "\n" + "etendue du capteur" + liste_cap[i][x-1][0] + " " + str(i+1) + " : " + str(max(liste_cap[i][x-1][2])-min(liste_cap[i][x-1][2]))[:6] +"\n")            
# if x== 2: 
#       for i in range (6):
#           print("max du capteur " + liste_cap[i][x-1][0] + " " + str(i+1) + " :",max(liste_cap[i][x-1][2]))