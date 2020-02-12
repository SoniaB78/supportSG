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

#Appel du module (il doit être à la racine)
import ModulePersonne as MP

#Instanciation
p = MP.Personne() #instanciation => fonction donc parenthèse

#Affiche tout les membres de p

print(dir(p))

p.saisies()

p.affichage()

p.retraite(62)

#p.augmentation()

liste = []

nbrPersonnesChoisi = int(input("nb de personne :"))
#créer une liste de personnes à partir de l'input  ~nbrPersonnesChoisi~
for nouvellePersonne in range(0, nbrPersonnesChoisi):
    a = MP.Personne()#instanciation
    a.saisies()#saisie des champs
    liste.append(a)#ajoute à la liste chaque personne avec ses entrées

print("*** debut affichage ***")

#affichage de la liste de personnes
for personnes in liste:
    print("-----")
    p.affichage()
"""

numero = int(input("N° ind à traiter :"))
#Modifiera le salaire en fonction de l'indice récupéré dans l'input
if (numero < len(liste)):#si le numéro est bien dans la liste (longueur)
    b = liste[numero] #affecte l'indice , JE NE COMPREND PAS EN FAIT....
    #
    b.salaire = b.salaire * 2

    print("xxx début d'affichage 2")
    for personnes in liste:
        print("-----")
        p.affichage()
else:
    print("indice non valable")

"""

augmentDeMasse = input("Voulez vous doubler le salaire de tout le monde?")
#demande si on veut *2 le salaie de tout le monde
if (augmentDeMasse == "oui"):# oui
    for personnes in liste:#parcours la longueure de la liste pour récupérer l'indice
        personnes.salaire = personnes.salaire * 2 #calcule pour le salaire
        personnes.affichage()
else:#non et tout le reste
    print("ok.")

