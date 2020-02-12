#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     10/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint
from tkinter import *

def initialisation_cartes():
    """Fonction permettant de mélanger le jeu de cartes"""
    liste_carte = [
    '2P','3P','4P','5P','6P','7P','8P','9P','10P','VP','DP','RP','AP',
    '2C','3C','4C','5C','6C','7C','8C','9C','10C','VC','DC','RC','AC',
    '2T','3T','4T','5T','6T','7T','8T','9T','10T','VT','DT','RT','AT',
    '2K','3K','4K','5K','6K','7K','8K','9K','10K','VK','DK','RK','AK'
    ]

    cartes_sorties = []

    return liste_carte, cartes_sorties

def pioche(liste_carte,cartes_sorties):
    """Pioche une carte aléatoirement dans les cartes disponibles.
    ENTREES :
        Liste des cartes dans la main
        Liste des cartes déjà sorties
    RETURN
        Une carte aléatoire

    """
    aleatoire = randint(0,len(liste_carte)-1)
    carte = liste_carte[aleatoire]
    del liste_carte[aleatoire]
    cartes_sorties.append(carte)
    return carte

def calcul_valeur(cartes_sorties):
    """Calcul la valeur des cartes dans la main
    ENTREES :
        Liste des cartes dans la main
    RETURN
        La valeur totale des cartes dans la main

    """

    sommeDesCartes = int()
    for carte in cartes_sorties:
        valeur_carte = carte[0]

        if valeur_carte == "A" or valeur_carte == "R" or valeur_carte == "D"\
        or valeur_carte == "V" or valeur_carte == "1":
            point = 10
        else:
            point = int(valeur_carte)
        sommeDesCartes += point
    return sommeDesCartes

def gain(sommeDesCartes,argent,mise):

    """Calcul des gains
    ENTREES :
        Somme des cartes dans la main
        Argent restant
        Mise
    RETURN
        Valeur des gains ou des pertes
    """

    if sommeDesCartes == 21:
        argent += (mise * 3)
    elif 18 <= sommeDesCartes <= 20:
        argent += (mise * 2)
    else:
        argent -= mise

    return argent

def main(argent):
  """Programme principal
  Boucle de jeu
  """

  input("""Bienvenue au MégaBlackJacky
  Règles:
    Les figures valent 10
    Misez et piochez des cartes
      Somme des cartes égale à 21 : 3X la mise
      Somme des cartes entre 18 et 20 : 2X la mise
      Somme des cartes supérieure à 21 : Merci pour l'argent
        Cliquez sur OK pour continuer.
   """)

  while argent > 0:
    continuer = "o"
    liste_carte, cartes_sorties = initialisation_cartes()
    pioche(liste_carte,cartes_sorties)
    pioche(liste_carte,cartes_sorties)
    sommeDesCartes = calcul_valeur(cartes_sorties)

    mise = abs(int(input("Il vous reste {} . Mise : ".format(argent))))
    if mise <= argent:
        if sommeDesCartes == 21:
            argent = gain(sommeDesCartes, argent, mise)
        else:
            while continuer =="o":
                sommeDesCartes = calcul_valeur(cartes_sorties)


                continuer = input("CARTES : {} \nSomme des cartes : {} \n\
Continuer (O/N)".format(cartes_sorties, sommeDesCartes))

                if continuer == "":
                    continuer = "o"

                if continuer == "o" or continuer == "o":
                    pioche(liste_carte,cartes_sorties)

                else:
                    argent = gain(sommeDesCartes, argent, mise)


  input("T'as tout perdu, tu l'as dans l'c...")







if __name__ == '__main__':
    argent = 100
    initialisation_cartes()


    main(argent)


