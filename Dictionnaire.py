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

def information_personne(p, n, a):
    print("\n Prénom :", p.capitalize(), ", Nom :", n.upper(), ", Age :", a)
    return p, n, a
    # si je return [p, n, a] cela retoune une liste qui est modifiable
"""
tuple1 = ("Michel")
tuple2 = ("Jacky & ")
tuple3 = tuple2 + tuple1
print(tuple3)
"""

def dictionnaire():
    capitale = {"France":"Paris","Allemagne":"Berlin"}
    liste_capitales = [("France","Paris"),("Allemagne","Berlin")]
    capitales = dict(liste_capitales)
    capitale["Espagne"] = "Madrid"
    print(capitales)
    ville = capitale["Espagne"]
    print(ville)
    r = capitales.get("Gilles", "Veronie")
    print(r)

    # pour vider la liste ==> capitales.clear()
    # pour connaitre la longueure ==> len(capitales)
    # pour connaitre la clef print(capitales.keys())
    #CRUD

if __name__ == '__main__':
    p = input("Veuillez entrer votre prénom")
    n = input("Veuillez entrer votre nom")
    a = input("Veuillez entrer votre age")
    #information_personne(p, n, a)
    dictionnaire()
