#-------------------------------------------------------------------------------
# Name:        conversion
# Purpose:     purple
# Author:     sonia
# Created:     12/06/2019
# Copyright:   (c) Gilles #boaf c'est tellement modifié...
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

fahrenheit = 0.0
input = 0.0

# Récupération de l'entrée, input, calcule et conversion en string
def calcule():
    celcius = int( input.get())
    fahrenheit = 9.0/5.0 * celcius + 32
    Texte.set(str(fahrenheit))


#global fahrenheit
# création de la fenetre
fenetre = Tk()
# titre DE la fenetre
fenetre.title('Celcius en Fahrenheit')

# titre DANS la fenetre
titre = Label(fenetre, text='Conversion C° --> F', fg='turquoise4')
titre.pack()

# INPUT INPUT
input = Entry(fenetre, width =45, bg='PaleTurquoise1')
input.pack()

# LABEL RESULTAT
Texte = StringVar()
resultat = Label(fenetre, width= 20, textvariable= Texte, fg= "black", bg= "white")
resultat.pack()

# BTN CALCULER
calculer = Button(fenetre, width =15, text='convertir', fg='gray1', bg='cyan2', command = calcule)
calculer.pack(side=LEFT)
# BTN QUITTER
quitter = Button(fenetre, width =15, text='quitter', fg='gray1', bg='cyan2', command = fenetre.destroy)
quitter.pack(side=RIGHT)

fenetre.mainloop()


#grid ne fonctionne pas bien avec les appels de fonction, programme pincipal pas forcément de def main
