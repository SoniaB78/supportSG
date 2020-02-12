#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     12/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
affiche la valeur de L[4]

modifie la liste en remplaçant L[1] par 17 et L[3] par la somme
des cases voisines L[2] et L[4]

affiche 12 fois la valeur du dernier terme de la liste
"""
#for entier in range(10):
   #print(entier, end = " ")
entier = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def liste():
    print("Exercice 1")
    print(entier[4])
    entier[1] = 17
    print(entier)
    entier[3] = entier[2] + entier[4]
    print(entier)
    for i in range(12):
        print(entier[-1], end="")
    print("\n")


"""
Écrire un programme qui échange les valeurs de la première et
de la dernière case d’une liste quelconque non vide.
"""
def liste2():
    print("Exercice 2")
    change = entier[0]#pour échanger deux valeurs stocker en une avant
    entier[0] = entier[-1]
    entier[-1] = change
    print(entier, "\n")

"""
Affiche la liste en colonne
Compte le nombre de multiples de 3 présents dans la liste
Calcule la somme de toutes les valeurs paires de la liste
Calcule le maximum et le minimum des éléments de la liste
Créer un booléen vraie si la moyenne arithmétique des valeurs de la liste est supérieure ou égale à 10
Créer le produit* de toutes les valeurs de la liste comprise dans l’intervalle [50, 70]
Affiche la liste à l’envers (sans créer de nouvelle liste)
"""
def liste3():
    print("Exercice 3")
    mltp = 0
    pair = 0
    moy = 0
    produit = 1
    for i in entier:
        #print(i)
        if i%3 == 0:#verifie multiple de 3
            mltp += 1
        if i%2 == 0:#vérifie pairs
            pair += i

        moy += i #somme des entrées du tableau
    moy  /= len(entier)#somme des entiers divisé par le nombre d'entrée
    print("La moyenne arithmétique des valeurs de la liste est-elle supérieure ou égale à 10", moy >= 10)#PUTAIN DE BOOLEAN !!

    print("Le nombre de multiples de 3 :", mltp, ", et la somme des pairs:", pair, "\n La valeur max est de: ", max(entier), ", la valeur min est de: ", min(entier))

    liste_produit = [50, 30, 24, 68, 76, 12, 5, 96]
    long = len(liste_produit)
    for i in range(0,long):
        if liste_produit[i] <= 70 and liste_produit[i] >= 50:
            produit *= liste_produit[i] #multiplie les i un a un des nombres situés entre 50 ET 70
    print("Le produit de tous les entiers situés entre 50 et 70 est:", produit)

    print(entier[::-1])# reverse mais avec les indices

"""
Modifie la liste en augmentant de 1 la valeur de chaque
élément de la liste
Modifie la liste par permutation circulaire
Modifie la liste par miroir
"""
def liste4():
    print("Exercice 4")
    long = len(entier)
    for i in range(long):
        entier[i] += 1
    print(entier)
#permutation circulaire croissant !

    change = entier[0] #stock la 1ere valeur
    for i in range (long) :
        if i < long-1: # i inf à la long de la liste moins 1
            entier[i] = entier[i+1]
        else:
            entier[-1] = change #récupère la val de 0 avant les changements
    print (entier)

#liste miroir
    axe = (long)//2
    for i in range (0, axe):
        if i < axe:
            change = entier[i]
        if i > axe:
            entier[i] = entier[long-i-1]
        entier[long-i-1] = change
    print (entier)


"""
1. On dispose d’une liste L non vide de nombres. Créer une liste LC
contenant les carrés des nombres de L.

2. L3 identiques à L1 dans laquelle on a supprimé la première valeur

3. L4 contenant les valeurs L1 puis celles de L2
"""
from math import *
def liste5():
    racine = []
    for i in entier:
        racine.append(i**2)
    print("La liste entier stockée dans racine :", racine)

    liste3 = []
    for i in range (1, len(entier)): #on supprime la première val
        liste3.append(entier[i])
    print ("list3 = ", liste3)

    liste4 = entier + racine #colle les deux listes dans liste4
    print("liste 4 :", liste4)
"""
Écrire un programme qui affiche si une liste est symétrique (liste identique à la liste à
l’envers).
"""
def liste6():
    print("Exercice 6")
    entierR = entier[::-1]

    for i in range (1):
        print("Listes symetriques :", entier == entierR[::-1])



if __name__ == '__main__':
    #liste()
    #liste2()
    #liste3()
    liste4()
    #liste5()
    #liste6()

