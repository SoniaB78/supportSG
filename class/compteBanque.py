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

global depot, retrait

class Compte:

    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def soldeRestant(self):
        print("Mme / Mr:", self.nom, "Le solde de votre compte est de ", self.solde, "€.")

    def retrait(self):
        retrait = float(input("Combien souhaitez vous retirer?"))
        if retrait < self.solde:
            self.solde -= retrait
        else:
            print("Impossible de retirer plus que le solde disponible sur le compte.")
        #return self.solde
        self.soldeRestant()

    def depot(self):
        depot = float(input("Combien souhaitez vous déposer?"))
        if depot > 5000:
            print("OK... J'appel la police, nous gardons l'argent.")
        self.solde += depot
        self.soldeRestant()

"""

def __add__(self):
    self.depot = float(input("Combien souhaitez vous déposer?"))
    self.solde += self.depot

def __sub__(self):
    self.retrait = float(input("Combien souhaitez vous retirer?"))
    self.solde -= self.retrait

"""


Dupont = Compte("Dupont", 1000)
Braunstein = Compte("Braunstein", 8000)
Lavillier = Compte("Lavillier", 2000)

Dupont.soldeRestant()