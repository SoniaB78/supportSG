#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     20/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Voiture():
    def __init__(self):
        """Constucteur de notre classe"""
        self.nombre_roues = 4
        self.nombre_fauteils = 1
        self.moteur = "propulsion"



ma_voiture1 = Voiture()

print("Ma voiture:", ma_voiture1.moteur)
print(ma_voiture1.nombre_roues)
print(ma_voiture1.nombre_fauteils, "\n")


class Citroen():
    def __init__(self):
        self.type_suspension = "Hydractives"
        self.logo = "Chevrons"
        self.marque = "Citroën"

ma_citroen = Citroen()

print("Ma citroen:", ma_citroen.type_suspension)
print(ma_citroen.logo)
print(ma_citroen.marque, "\n")


class BondBug(Voiture):
    def __init__(self):
        """Hériage de voiture"""
        Voiture.__init__(self)
        self.modele = "Bug"
        self.marque = "Bond"
        self.nombre_roues = 3
        self.nombre_fauteils = 2

ma_bug = BondBug()

print("Ma bug:", ma_bug.nombre_fauteils)
print(ma_bug.moteur)
print(ma_bug.marque)
print(ma_bug.nombre_roues, "\n")

class CitroenDs(Voiture, Citroen):
    def __init__(self):
        Voiture.__init__(self)
        Citroen.__init__(self)
        self.modele = "DS de 1967"

ma_super_DS = CitroenDs()

print("Ma super DS:", ma_super_DS.nombre_roues)
print(ma_super_DS.logo)
print(ma_super_DS.marque, "\n")

class CitroenC4(Voiture, Citroen):
    def __init__(self):
        Voiture.__init__(self)
        Citroen.__init__(self)
        self.couleur = "rouge"
        self.conducteur = "Florent"

sa_citroen = CitroenC4()

print("Sa citröen:", sa_citroen.nombre_roues)
print(sa_citroen.logo)
print(sa_citroen.couleur, "\n")