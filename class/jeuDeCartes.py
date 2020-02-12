#-------------------------------------------------------------------------------
# Name:        jeuDeCarte
# Purpose:
#
# Author:
#
# Created:     20/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint
from random import shuffle

class Carte():
    def __init__(self):
        #liste préremplie.
        """
        self.liste_carte = [
        '2P','3P','4P','5P','6P','7P','8P','9P','10P','VP','DP','RP','AP',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','VC','DC','RC','AC',
        '2T','3T','4T','5T','6T','7T','8T','9T','10T','VT','DT','RT','AT',
        '2K','3K','4K','5K','6K','7K','8K','9K','10K','VK','DK','RK','AK'
        ]
        """
        self.valeur_carte = [2,3,4,5,6,7,8,9,10,'As','Valet','Dame','Roi']
        self.couleur_carte = ['Coeur','Pique','Carreau','Trèfle']



class jeuDeCarte(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.liste_carte = []
        self.liste_carte_retire = []
        self.carte = ""

    def creationJeu(self):
        for i in self.couleur_carte:
            for j in self.valeur_carte:
                self.liste_carte.append([i,j])

    def nom_carte(self):
        if self.tirer_carte() == True or self.afficher() == True:
            print(carte)
        else:
            print("Vous n'avez pas tiré de carte")

    def battre(self):
        #sample(x, k=len(x))
        shuffle(self.liste_carte)
        print("le jeu est battu")

    def afficher(self):
        if len(self.liste_carte) ==0 :
            print("Il n'y a plus de cartes...")
        else:
            for i in self.liste_carte:
                print(i,"\t" , end= "")
            return True

    def tirer(self):
        self.aleatoire = randint(0,len(self.liste_carte)-1)
        self.carte = self.liste_carte[self.aleatoire]
        self.liste_carte_retire.append(self.carte)
        del self.liste_carte[self.aleatoire]

        return self.carte


#-----------------------------PROGRAMME PRINCIPAL-----------------------------
#instanciation
j=jeuDeCarte()

#Création du jeu de cartes
j.creationJeu()

#présentation du jeu de carte
print("Le Jeu de carte est le suivant \n")
j.afficher()

#on mélange le jeu de carte
print("Le Jeu de carte est mélangé \t")
j.battre()

#puis on affiche
j.afficher()
print(len(j.liste_carte))
print(len(j.liste_carte_retire))
#on retire une à une toutes les cartes du jeu en montrant leur valeur

for i in range(0,len(j.liste_carte)):

    print("\t On retire une carte du jeu \t")
    j.tirer()
    print("La carte retirée est: ", j.carte,"\t")

#on affiche la liste de cartes retirées
print("Les cartes retirée sont:", j.liste_carte_retire)

#on affiche la liste de carte, mais comme celle-ci est vide on nous l'indique
j.afficher()

