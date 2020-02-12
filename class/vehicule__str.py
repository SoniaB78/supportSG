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
    def __init__(self,marque="Ford"):
        self.marque = marque
        self.modele = "Kuga"
        self.gamme = "ST line"

    def __str__(self):
        # objet ==> string
        return "{0} {1} {2}".format(self.marque, self.modele, self.gamme)

class VoitureCab(Voiture):
    #class cabriolet, hérite de Voiture
    def __init__(self, marque, gamme, structure_toit, couleur_toit, type_vehicule):
        Voiture.__init__(self, marque)
        self.type_vehicule = type_vehicule
        self.structure_toit = structure_toit
        self.couleur_toit = couleur_toit
        self.marque = marque

    def __str__(self):
        return "Marque{0}, stucture du toit{1}, couleur du toit: {2}, modele: {3}, gamme: {4}".format(self.structure_toit, self.couleur_toit, self.type_vehicule, self.gamme)



if __name__ == '__main__':
    vehicule1 = Voiture()
    vehicule2 = VoitureCab("Ford","aluminium", "noir", "SUV", "ST line")

    print(vehicule1.modele)
    print(vehicule2.couleur_toit)
