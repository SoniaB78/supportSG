#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     09/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#La boucle while sert  comparer
def devinette():
    from random import randint
    ch = -1 #-1
    nb = randint(1,10)
    while nb != ch: #tant que nb est différent de ch
        ch = int(input('Entrez un nombre entier entre 0 et 10'))
        if ch < nb: print('Trop petit')
        if ch > nb: print('Trop grand')
    print('Bravo')

    """
    i = 1
    while i <= 4:
        print (i)
        i = i + 1
    """
print ("\n")

# 1
organisme= ['vache', 'souris', 'levure', 'bacterie']
print (organisme)

for o in organisme:
    print(o)

print ("\n")
for o in range(4):
    print(organisme[o])


print ("\n")
o = 0
while o < len(organisme):
    print (organisme[o])
    o += 1

print ("\n")

semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for j in semaine:
    print(j)

print ("\n")
j = 0
while j < len(semaine):
    if j ==5 or j == 6: print (semaine[j])
    j += 1

print ("\n")
for i in range(1,11):
    print(i, end="")

print ("\n")
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
for i in impairs:
    print(i+1)

print ("\n")
note = [14, 9,6, 8, 12]
from statistics import mean
moyenne = mean(note)
print("%.*f" %(2,moyenne))

print ("\n")
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(4):
    produit = X[i] * X[i+1]# on multiplie grace à l'indice de l'itm réupéré par i
    #et pour avoir la deuxième valeur on fait i+1
    print(produit)

print ("\n")



if __name__ == '__main__':
    #devinette()
    #main()
    pass