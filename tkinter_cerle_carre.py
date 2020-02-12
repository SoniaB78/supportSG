#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     23/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from random import *


fenetre=Tk()
fenetre.title("diagonales")
fenetre.geometry("200x200")

canvas = Canvas(fenetre, width=200, height=200)

ligne1 = canvas.create_line(20, 20, 180, 20, width= 2, fill='turquoise2')
ligne2 = canvas.create_line(180, 20, 180, 180, width= 2, fill='turquoise2')
ligne3 = canvas.create_line(180, 180, 20, 180, width= 2, fill='turquoise2')
ligne4 = canvas.create_line(20, 180, 20, 20, width= 2, fill='turquoise2')

canvas.create_rectangle(50,50,150,150, width= 2, outline= "PaleTurquoise3")

canvas.create_oval(50,50,150,150, width= 2, outline= "turquoise4")

ligne5 = canvas.create_line(65, 65, 135, 135, width= 2, fill='aquamarine2')
ligne6 = canvas.create_line(65, 135, 135, 65, width= 2, fill='aquamarine2')

canvas.pack()

fenetre.mainloop()