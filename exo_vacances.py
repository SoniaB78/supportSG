#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     06/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def controlFluxGestion(flottant, mot1, mot2):
# question 1 :
    flottant = flottant
    if flottant >= 0:
        integer = int(flottant) # sinon {:.2f}
        print(integer)
    else:
        print(flottant, "n'est pas égal ou supérieur à 0")

# question 2 :
    mot1 = mot1
    mot2 = mot2
    if len(mot1) < len(mot2):
        print('"', mot1, "est plus petit que", mot2, '"')
    else:
        print('"', mot2, '"est plus petit que"', mot1, '"')
    #print('"', mot1, "est plus petit que", mot2, '"') if len(mot1) < len(mot2) else print('"', mot2, '"est plus petit que"', mot1, '"')

# question 3 :
    pSeuil = 2.3
    vSeuil = 7.41
    pression = float(input("Veuillez entrer une pression"))
    volume = float(input("Veuillez entrer un volume"))
    if pression > pSeuil and volume > vSeuil:
        print("ARRET IMMEDIAT")
    elif pression > pSeuil:
        print("Veuillez entrer une pression inférieure à", pSeuil)
    elif volume > vSeuil:
        print("Veuillez entrer un volume inférieure à", vSeuil)
    else:
        print("Tout va bien")

# question 4 :
    a, b = 0, 10
    while a < b:
        a += 1
        print(a)
    while b != 0:
        if b%2 == 0:
            print(b)
        b -= 1

# question 5 :
    n = int(input('Entrez un entier [1 .. 10] : '))
    while not(1 <= n <= 10) :
        n = int(input('Entrez un entier [1 .. 10], S.V.P. : '))

# question 6 :
    string = "chaine de charactere"
    for i in string:
        if i != " ":
            print(i, end = " ")

    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in liste:
        print(i)

# question 7 :
    for i in range(1, 15):
        if i%3 ==0:
            print(i)

# question 8 :
    for i in range(1, 10):
        if i == 5:
            break

# question 9 :
    for i in range(0, 10):
        if i == 5:
            continue
        print(i)
# question 10 :
    from math import sin
    for i in range(-3, 4):
        try:
            print("{:.3f}".format(sin(x)/x), end=" ")
        except:
            print("{:.3f}".format(float(1)), end=" ")
    print()

# easygui poour utiliser une version inf de python et ulitiser msgbox(input)
# // pour avoir le quotient(diviseur) % pour avoir le reste

# question 3-3:
    """#attention easygui ne fonctionne pas sur cette version
a = floatbox("Borne inferieur: ", "", 0.0, -100.0, 100.0)
b = floatbox("Borne supérieur :", "", a+.1, a)
n = integerbox("Nombre de pas ", "", 10, 0)
from easygui import floatbox, integerbox

def maFontion(x):
    return 2*x**3 +x - 5

def lesFonctions(fonction, borneInf, borneSup, nbPas):
    h = (borneSup - boneInf) / float(nbPas)
    x = borneInf
    while x <= borneSup:
        y = fonction(x)
    print("f({:.2f}) = {:.3f}".format(x, y))
    x += h
"""

truc = []
machin = [0.0, 0.0, 0.0, 0.0, 0.0]
print(truc, machin)

for i in range(0,3):
    print(i)
for i in range(4,7):
    print(i)
for i in range(2,8):
    if i%2 != 0:
        print(i)

chose = [ 0, 1, 2, 3, 4, 5]
for i in chose:
    if i == 3 or i ==6:
        print("true")

listencomprehension =[i+3 for i in range(0,5)]

listencomprehension2=[i+3 for i in range(0,5) if i >= 2]

abc = "abc"
de = "de"
abcde =[j+i for j in abc for i in de]
print(abcde)


somme = sum([i for i in range(0,10)])
print(somme)




if __name__ == '__main__':
    #ontrolFluxGestion(2.6,"chaine","charactere")
    #lesFonctions(maFonction,a, b, n)
    pass

