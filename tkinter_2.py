#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sonia
#
# Created:     23/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from random import *

def NouveauLance():
    nb=randint(1,6)


#création de la fenêtre principale (main window)
Mafenetre=Tk()

Mafenetre.geometry("150x150")
Mafenetre.configure(background='PaleTurquoise1')

Mafenetre.title("Dé à 6 faces")

#création d'un widget Button (bouton lancer)
BoutonLancer = Button(Mafenetre, width= 20, text= 'lancer', fg= 'gray1', bg= 'cyan2', command= NouveauLance)
#.wrap .pack .grid (pack pour reste sur la fenetre,
#Positionnement du widget avec la méthode pack ()
BoutonLancer.pack(side= TOP, padx= 10, pady= 10)

#Création d'un widget label (texte "résultat -> x")
Texte = StringVar()
Texte.set ("résultat -> "+ str(nb))
LabelResultat=Label(Mafenetre, width= 20, textvariable= Texte, fg= "turquoise4", bg= "white")
LabelResultat.pack(side= TOP, padx= 5, pady= 5)

#création d'un widget Button (bouton Quitter)
BoutonQuitter=Button(Mafenetre, width= 20, text= "quitter", bg= 'cyan2', command= Mafenetre.destroy)
#Positionnement du widget avec la méthode pack ()
BoutonQuitter.pack(side= TOP, padx= 10, pady= 10)

#On appelle une fois la fonction pour initialiser notre Texte
NouveauLance()

Mafenetre.mainloop()