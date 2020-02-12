#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     07/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
nombreATester = 13
rangeListe = int(nombreATester)
listeDiv = []
for i in range(1, rangeListe):
    if nombreATester % i == 0:
        listeDiv.append(i)
print(listeDiv)

def somDiv():
    global somme
    for i in listeDiv:
        somme += i
    return somme

def estParfait():
    global somme
    if somme == nombreATester:
        return True

def estPremier():
    if len(listeDiv) == 1 :
        for i in range(0, len(listeDiv)):
            if i == 1 or i == nombreATester :
                return True

def estChanceux():
    impairs = []
    global nombreATester
    for i in range(1, nombreATester):
        if i % 2 != 0:
            impairs.append(i)
        for j in impairs:
            if j % i == 0:
                impairs.remove(j)
    if j == nombreATester:
        return True
        print(nombreATester, " est un nombre chanceux")
    else:
        print(nombreATester, " n'est pas un nombre chanceux")

def autoTest():
    pass


if __name__ == '__main__':
    somme = 0
    somDiv()
    estParfait()
    estPremier()
    estChanceux()
    #pass
