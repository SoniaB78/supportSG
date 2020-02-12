#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     09/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Personne:
    """ Classe Personne """
    # constructeur
    def __init__(self): #self représente l'instance
        # liste d'attributs

        self.prenom = ""
        self.age = 0
        self.salaire = 0.0
        self.tpsEnPoste = 0

    def saisies(self):
        #Affectation aux champs
        self.prenom = input("Entrez vôtre prénom : ")
        self.age = int(input("Entrez vôtre age : "))
        self.salaire = float(input("Entrez vôtre salaire : "))
        self.tpsEnPoste = float(input("Depuis combien de temps travaillez vous dans l'entreprise ? (en mois) "))

    #Affichage
    def affichage(self):
        print("Prénom:", self.prenom,", age: ", self.age, ", salaire: ", self.salaire, "mois en poste:", self.tpsEnPoste)

    def retraite(self, limite):
        reste = limite - self.age
        if (reste < 0):
            print("Vous ètes à la retraite")
        else:
            print("Il vous reste %s années avant la retraite."%(reste))

    def __add__(self):
        if self.tpsEnPoste >= 6:
            print("Vous avez passé 6mois ou plus à ce poste, nous avons pensé à vous donner une augmentation.")
            self.salaire += 100
        elif self.tpsEnPoste < 6 and self.tpsEnPoste > 1:
            print("Continuez de bien faire votre travaille et dans quelques temps on vous augmentera.")
        elif self.tpsEnPoste < 1 :
            print("Bienvenue dans l'entreprise !")


