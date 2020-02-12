#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     04/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#toujours nom de fonctions différents
def somme(n):
    s = 0
    for i in range(n+1): # n+1 pour avoir le dernier tour == 11 au lieu de 10
        s += i
    return s

def compte(n):
    c = 5000
    for i in range(n):
        c = (c*(1+0.025)).__round__ (2) #arrondie à 2 après la virgule
        #>>> from decimal import Decimal
        #>>> print Decimal(str(round(9.941,2))) --> 9.94

    return c


#table de neuf avec range
def table():
    i = 1 #itérations
    j = 1 #itérations
    for i in range(0, 10): #on va faire 10 tours pour les 10 tables
        i+=1 # rajoute une itération
        print("TABLE DE ", i)
        for j in range(0, 10):
            j+=1 # rajoute une itération
            print (i, "*", j, "=", i*j) #utilise le i pour multiplier le nbr
        print("\n")

#nombre de nombres pairs entre 0 et 1000.
def nombrePairs():
    #pas besoin de définir pairs
    # range(début, fin, par)

    count = 0 #ncompte le nombre de chiffres pairs
    for pairs in range(2, 1000):
        # checking condition
        if pairs % 2 == 0: # vérifie si ce nombre divisé par 2 n'a pas de reste
            count += 1 #rajoute une itération

    print("Il y a ", count, "nombres pairs dans 1000")

from random import randint
#Lancement d'un dé à six faces
def de(n):
    nbre_six = 0
    for i in range(n):
        if randint(1,6) == 6:#lance le dé de 1 à 6 compte les 6
            nbre_six += 1
    return nbre_six
#randint lance en aléatoire donc les résultats sont toujous différents

# toujous à la fin
if __name__ == '__main__':
    #main()
    #print(somme(4))
    #print(compte(2))
    print(table())
    #print(nombrePairs())
    #print(de(25))