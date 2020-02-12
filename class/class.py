#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     08/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Class_vide:
    pass

cl = Class_vide()

print(type(cl))
print(isinstance(cl, Class_vide))

class Chien:
    #Ma classe chien
    def __init__(self, Race, Nom, Couleur, Taille):
        self.Race = Race
        self.Nom = Nom
        self.Couleur = Couleur
        self.Taille = Taille

    def Jappe(self):
        print("*Le chien jappe*")

monChien1 = Chien("Beagle", "Trix", "maron", "petit")
monChien2 = Chien("Setter", "Nina", "noir", "grande")
monChien3 = Chien("Golden", "Max", "beige", "grande")
monChien4 = Chien("Bosron", "Xenon", "noir", "moyen")
print(monChien1.Nom)
print(monChien2.Race)



