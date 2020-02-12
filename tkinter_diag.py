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

ligne1 = canvas.create_line(200, 0, 0, 200, width= 2, fill='turquoise4')

ligne2 = canvas.create_line(0, 0, 200,200, width= 2, fill='turquoise4')

canvas.pack()
fenetre.mainloop()s