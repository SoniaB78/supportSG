#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:     gilles
#
# Created:     12/06/2019
# Copyright:   (c) Gilles

# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Lien en Francais sur Tkinter --> http://tkinter.fdex.eu/index.html

from tkinter import *       # Importation du module Tkinter
                            # Ce module est déjà intégré à Python 3

def calcul():
    # Définir les variables globales
    global textI
    global textO

    i = textI.get()               # Recupère la saisie de textI
    textO.delete(0, END)          # Supprime le contenu de textO
    for c in textI.get():         # Boucle sur chaque caractère
        # Si c en maj, le transforme en minus, sinon l'inverse
        # insertion du caractère modifié dans la zone de saisie de droite
        textO.insert(END, c.upper()) if c.islower() else textO.insert(END, c.lower())

def main():
    # Définir les variables globales
    global textI
    global textO

    fen1 = Tk()                     # Création de l'instance de la fentetre
    fen1.title('TkInter bases')    # Modification du titre de la fenetre Windows
    # Création des composants (Widgets) dans la fenetre
    titre = Label(fen1, text='Tkinter', fg='turquoise4')       # Libéllé
    textI = Entry(fen1,width =45, bg='PaleTurquoise1')          # Saisie
    textO = Entry(fen1,width =45, bg='PaleTurquoise1')           # Saisie
    bou_exit = Button(fen1,width =15, text='Close', fg='gray1', bg='cyan2', command = fen1.destroy)   # Bouton
            # "command = fen1.destroy" permet de détruire l'instance,
            # et donc fermer la fenetre
    bou_calcul = Button(fen1,width =15,text='Maj', fg='gray1', bg='cyan2', command = calcul)          # Bouton
            # "command = calcul" va éxecuter la fonction "def calcul()"

    # Placement des composants graphiques dans la fenetre
    # Découpage de la fenetre en 2 columns et 3 rows
    titre.grid(row=1,column=1,sticky=N,columnspan=2)     # L0,centré sur 2 colonnes
    textI.grid(row=2,column=1,sticky=W)         # L1,C1, cadré à Gauche
    textO.grid(row=2,column=2,sticky=E)         # L1,C2, cadré à Droite
    bou_exit.grid(row=3,column=1,sticky=N)      # L2,C1, Centré
    bou_calcul.grid(row=3,column=2,sticky=N)    # L2,C2, Centré

    fen1.mainloop()         # Boucle sur les événements

if __name__ == '__main__':
    main()