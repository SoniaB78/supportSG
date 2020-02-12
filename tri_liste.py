#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     13/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def tri():
    liste = [0,6,1,0,9,7,8,5,7,3] #ordre voulu 0013567789
    long = len(liste)
    change = 0
    for i in range(long-1):
        for j in range(long-1):
            if liste[j] > liste[j+1]:
                change = liste[j+1]
                #liste[j+1],liste[j] = liste[j],liste[j+1]
                liste[j+1] = liste[j]
                liste[j] = change
    print(liste)


def triprompt():
    liste = list(input("Rentrez des nombres entiers").split(" "))
    print(liste)
    long = len(liste)
    change = 0
    for i in range(long-1):
        for j in range(long-1):
            if liste[j] > liste[j+1]:
                change = liste[j+1]
                #liste[j+1],liste[j] = liste[j],liste[j+1]
                liste[j+1] = liste[j]
                liste[j] = change
    print(liste)

def trirapide():
    liste = [0,6,1,0,9,7,8,5,7,3]
    long = len(liste)
    linf = []
    lsup = []
    for i in liste:
        pivot = liste[long%2]
        if i < pivot:
            linf.append(i)
        if i > pivot:
            lsup.append(i)

    print(lsup)#[1, 2, 3, 4, 5, 6, 7, 8, 9] pourquoi linf vide?


import random

"""
générer une liste aléatoire en compréhension de liste
liste = [random.randint(0, 10) for i in range(8)]
print(liste)
"""
def listrandom():
    liste = [random.randint(0,20) for i in range(20)]
    print(liste)
    for j in range(len(liste)-1):

        if liste[j] > liste[j+1]:
            liste[j], liste[j+1] = liste[j+1],liste[j]


    print(liste)

def tri_selection(liste):
    liste = [random.randint(0,20) for i in range(20)]#créer un liste aléatoire
    m = len(liste) #pour avoir la longueur de la liste en int

    for i in range(0, m):
        min = i
        for j in range(i+1, m): #on regarde l'item suivant et on retourne le plus petit
            if liste[j] < liste[min]: #si la valeur de j est inf à la valeur de i/min
                min = j #min devient j
        if min is not i: #
            nb = liste[i]
            liste[i] = liste[min]
            liste[min] = nb
    print(liste)

"""
def triFlorent(liste):
    listeTriee = [] #Initialisation liste vide de sortie
    for i in range(len(liste)):
        mini = min(liste) #Récupération de la valeur mini de la liste
        place = liste.index(mini) #Récupération de l'index de la valeur mini
        listeTriee.append(mini) #Ajout de la valeur mini dans la liste de sortie
        del liste[place] #Suppression de la valeur mini dans la liste initiale
    return listeTriee #Renvoie la liste triée


print(liste)
listeTriee = triFlorent(liste)
print(listeTriee)
"""
def tri_insertion(liste):
    liste = [random.randint(0,20) for i in range(20)] #créer un liste aléatoire
    n = len(liste)
    for j in range(1, n):
        x = liste[j]
        while j > 0 and liste[j-1] > x:
            liste[j] = liste[j - 1]
            j -= 1
        liste[j] = x
    print(liste)
    return liste



if __name__ == '__main__':
    #tri()
    #triprompt()
    #trirapide()
    #listrandom()
    #tri_selection(20)
    tri_insertion(20)
    #pass