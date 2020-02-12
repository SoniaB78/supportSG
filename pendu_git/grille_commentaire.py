#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      haya_
#
# Created:     23/12/2019
# Copyright:   (c) haya_ 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from tkinter import *  # import tkinter (pour le visuel)
import pandas as pd  # import de pandas (pour tableaux)
from random import *  # import de random
import numpy as np  # import de numpy (pour listes et tableaux)
from PIL import Image # Importation de pillow


data=pd.read_csv("fruit.txt",header=None)  # via pandas on telecharge le fichier txt
window=Tk() # on crée un objet windows
window.config(background="black")
window.geometry("700x700")
frame2=Frame(window,height=20,width=20)
frame2.pack(side=TOP,expand=YES)


def envoi():

    root2=Toplevel() # Toplevel() ouvre une nouvelle fenêtre
    root2.geometry("600x300") # paramètre des pixels de la fenêtre

    root2.title("choix du thème")


    photo = PhotoImage(file='chiens.png')  # photoimage permet de lire une image

    photo3= PhotoImage(file='fruits2.png')
    photo4= PhotoImage(file='ferme2.png')
    photo5= PhotoImage(file='pays2.png')
    button = Button(root2, image=photo,command=quitter)
    button.grid(row=1,column=0)  # grid permet de séparer la fenêtre en une grille de X row et Y col et de positionner les objets
    button = Button(root2, image=photo3,command=quitter)
    button.grid(row=1,column=1)
    button = Button(root2, image=photo4,command=quitter)
    button.grid(row=0,column=0)
    button = Button(root2, image=photo5,command=quitter)
    button.grid(row=0,column=1)

    root2.mainloop() # on lance Tkinter et ce qui a été créé précédemment





a=randint(0,data.shape[0]-1)
mot=data.iloc[a,0] # iloc permet de récupérer les lignes de notre tableau "data" aléatoirement
def tiret(mot):
    for i in range(len(mot)):
        label=Label(frame2,text='____',bg='black',fg='white')
        label.grid(row=200,column=i)



tiret(mot)
u=0
w=0
v=0
#creation de la page 4
print(mot)
def lettre(c,mot,bouton):
    global u  # variable globale : elle peut être appelée à l'extérieur de la fonction
    global w
    global v
    mot=mot.upper() # les lettres du mot sont converties en majuscules
    print(len(mot))
    s=0
    for t,i in enumerate(mot):

        if c in i: # si la lettre est dans le mot

            e=Entry(frame2,bg="black",fg="red",width=3,bd=0,font=('Helveticia', '12', 'bold'))

            e.grid(row=200,column=t)
            e.delete(0,END)
            e.insert(0,c)

            w=w+1 # w compte le nombre de bonnes lettres
            print(w)
            bouton.destroy() # la lettre du clavier est supprimée
        else: # si la lettre n'est pas dans le mot
            s=s+1 # s : compte les erreurs
            if s==len(mot):
                v=v+1 # v : compte les erreurs
            bouton.destroy()
    u=u+1

# si toutes les lettres sont trouvées
    if w==len(mot)  :

        root=Toplevel()
        root.config(background="black")
        root.geometry("800x800")



        frame5=Frame(root,bg="black")
        frame5.pack(side=TOP)
        Label2=Label(frame5,text="Super, le mot est ",font=('Times', '40', 'bold italic'),bg="black" ,fg="blue")
        Label3=Label(frame5,text=mot,font=('Times', '40', 'bold '),bg="black" ,fg="white")
        Label2.grid(row=0,column=0)
        Label3.grid(row=1,column=0)
        photo5= PhotoImage(file="{}.png".format(mot)).subsample(3)
        canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
        canvas.create_image(100,100,image=photo5)
        canvas.grid(row=2,column=0)
        photo4= PhotoImage(file='bravo.png').subsample(2)

        canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
        canvas.create_image(100,100,image=photo4)
        canvas.grid(row=5,column=0)
        titre=Label(frame5,text="Bravo tu as gagné!!!",font=("Helveticia",25,'bold italic'),bg="black",fg="red")
        titre.grid(row=6,column=0)
        frame.pack(expand=YES)
        bouton7=Button(root,text="Quitter",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=quitter)
        bouton7.pack(side=RIGHT)
        bouton2=Button(root,text="Rejouer",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=envoi)
        bouton2.pack(side=LEFT)
        root.mainloop()







# si on atteint le nombre de 5 erreurs
    if v>4:

        root=Toplevel()
        root.config(background="black")
        root.geometry("800x800")



        frame5=Frame(root,bg="black")
        frame5.pack(side=TOP)
        Label2=Label(frame5,text="Pfff, le mot était ",font=('Times', '40', 'bold italic'),bg="black" ,fg="blue")
        Label3=Label(frame5,text=mot,font=('Times', '40', 'bold '),bg="black" ,fg="white")
        Label2.grid(row=0,column=0)
        Label3.grid(row=1,column=0)
        photo5= PhotoImage(file="{}.png".format(mot)).subsample(3)
        canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
        canvas.create_image(100,100,image=photo5)
        canvas.grid(row=2,column=0)
        photo4= PhotoImage(file='bidon2.png').subsample(2)

        canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
        canvas.create_image(100,100,image=photo4)
        canvas.grid(row=5,column=0)
        titre=Label(frame5,text="Gros Nazzzz!!!",font=("Helveticia",25,'bold italic'),bg="black",fg="red")
        titre.grid(row=6,column=0)
        frame.pack(expand=YES)
        bouton7=Button(root,text="Quitter",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=quitter)
        bouton7.pack(side=RIGHT)
        bouton2=Button(root,text="Rejouer",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=envoi)
        bouton2.pack(side=LEFT)
        root.mainloop()


# fonction quitter
def quitter():
    global root
    window.destroy()

frame=Frame(window,bg="black",height=10,width=10)

frame.pack(expand=YES)

# lambda est une fonction temporaire qui permet d'executer la fonction lettre (suppression quand sélection)
A=Button(frame,text="A",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("A",mot,A))

Z=Button(frame,text="Z",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("Z",mot,Z))
E=Button(frame,text="E",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("E",mot,E))
R=Button(frame,text="R",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("R",mot,R))
T=Button(frame,text="T",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("T",mot,T))
Y=Button(frame,text="Y",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("Y",mot,Y))
U=Button(frame,text="U",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("U",mot,U))
I=Button(frame,text="I",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("I",mot,I))
O=Button(frame,text="O",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("O",mot,O))
P=Button(frame,text="P",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("P",mot,P))
Q=Button(frame,text="Q",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("Q",mot,Q))
S=Button(frame,text="S",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("S",mot,S))
D=Button(frame,text="D",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("D",mot,D))
F=Button(frame,text="F",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("F",mot,F))
G=Button(frame,text="G",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("G",mot,G))
H=Button(frame,text="H",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("H",mot,H))
J=Button(frame,text="J",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("J",mot,J))
K=Button(frame,text="K",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("K",mot,K))
L=Button(frame,text="L",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("L",mot,L))
M=Button(frame,text="M",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("M",mot,M))
W=Button(frame,text="W",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("W",mot,W))
X=Button(frame,text="X",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("X",mot,X))
C=Button(frame,text="C",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("C",mot,C))
V=Button(frame,text="V",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("V",mot,V))
B=Button(frame,text="B",bg="black",fg="white",padx=10,pady=10,command=lambda:lettre("B",mot,B))
N=Button(frame,text="N",fg="white",bg="black",padx=10,pady=10,command=lambda:lettre("N",mot,N))
espace=Button(frame,text="espace",fg="white",bg="black",padx=14,pady=10,command=lambda:lettre(" ",mot,espace))







# positionnement des lettre sur le clavier
A.grid(column=0,row=0)
Z.grid(column=1,row=0)
E.grid(column=2,row=0)
R.grid(column=3,row=0)
T.grid(column=4,row=0)
Y.grid(column=5,row=0)
U.grid(column=6,row=0)
I.grid(column=7,row=0)
O.grid(column=8,row=0)
P.grid(column=9,row=0)
Q.grid(column=0,row=1)
S.grid(column=1,row=1)
D.grid(column=2,row=1)
F.grid(column=3,row=1)
G.grid(column=4,row=1)
H.grid(column=5,row=1)
J.grid(column=6,row=1)
K.grid(column=7,row=1)
L.grid(column=8,row=1)
M.grid(column=9,row=1)

W.grid(column=0,row=2)
X.grid(column=1,row=2)
C.grid(column=2,row=2)
V.grid(column=3,row=2)
B.grid(column=4,row=2)
N.grid(column=5,row=2)
espace.grid(column=6,row=2,columnspan=2)



window.mainloop()