#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     03/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# génération de listes d'entiers: range()
# de n à n-1
print(list(range(2,10)))

animaux=['girafe', 'tigre', 'singe', 'souris']
tailles = [5, 2.5, 1.75, 0.15]
mixte = [ 'girafe', 5, 'tigre', 2.5, 'singe', 1.75, 'souris', 0.15]

print("\n",mixte, "\n", tailles, "\n", animaux)

# l'indice est la position d'un item dans la liste n à n-1
print(animaux[0])

gabaritsAnimaux = animaux + tailles
print(gabaritsAnimaux * 3, "\n")

print(animaux[-1])
# -4 -3 -2 -1 alors que  0 1 2 3

print(animaux[0:2])
print(animaux[0:3])
print(animaux[0:])# liste[début:fin], si on ne met rien celà prend l'extremité
print(animaux[:])# pend tout
print(animaux[:1])
print(animaux[1:-1], "\n")#le dernier 'souris' n'est pas prit en compte

#FORMATAGE

a = "mais"
b = "Non"
c = "allo"
d = "quoi"
message = "%s %s %s %s !" % (b, a, c, d)#tansforme en liste
print(message)
# ajoute un espace entre les variables et permet de changer l'ordre

e = message[4:13]
print("'", e, "'", "\n")
#n'affiche que "mais allo"

enclos1 = ['girafe', 4]
enclos2 = ['tigre', 2]
enclos3 = ['singe', 5]
enclos4 = ['lion', 3]
zoo = [enclos1], [enclos2], [enclos3], [enclos4]

print(zoo)

print(zoo[1])
#tigre 2

print(zoo[1][0])
#tigre 2

#print(zoo[1][1])
# ne fonctionne pas car le deuxieme 1 est out of range
#car le dernier nomé est exclu?

print(zoo[3][0], "\n")

semaine=['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
print("Les jours de la semaine sont :", semaine[0:5])
print("Le weekend est :", semaine[-2], semaine[-1])
print("Le dernier jour de la semaine est :", semaine[-1], "ou encore.... ", semaine[6])
semaine.reverse() # [::-1] est l'équivalent, sinon list.reverse()
print("La semaine inversée", semaine, "\n")

hiver = ["decembre", "janvier", "février"]
printemps = ["mars", "avril", "mai"]
ete = ["juin", "juillet", "août"]
automne = ["septembre", "octobre", "novembre"]
saisons = [hiver], [printemps], [ete], [automne]

print("saisons[2]", saisons[2]) #[['juin', 'juillet', 'août']]
# j'avais dis été mais n'était pas sure que ça afficherait le contenu du
#deuxieme tableau
print("saisons[1][0]", saisons[1][0]) #['mars', 'avril', 'mai']
# j'avais mis printemps mars, mais ça affiche tout...
print("saisons[1:2]", saisons[1:2]) #([['mars', 'avril', 'mai']],)
#j'avais mis printemps , mais en fait ça donne le contenu
print("saisons[:][1]", saisons[:][1], "\n") #[['mars', 'avril', 'mai']]
#j'avais mis toutes les saison et l'id 1 de chaque... NOPE!!

# quand on appel un tableau multidimensionnel comme "saison"
# saison[contient la première variable][contient une chaine de charactère]
# Les cochets contiennent la valeur de la variable indiquée.

print(animaux)#toute la liste

print(animaux[1:3])#SLICE on affiche le 2 et le 3

for i in animaux[1:3]:#BOUCLE dans le SLICE
    print(i)

print(i, "\n")#affiche singe

for i in range(0, 4):#(in range(4) == in range(0, 4)
    print(animaux[i], "\n")#print(i) affiche 0 1 2 3

for animal in animaux:
    print(animal, "\n")

# xrange n'existe plus

# enumarate affiche les ID devant les items
# boucle imbriquée
for i, ani in enumerate(animaux):
    print (i, ani)

print("\n")
liste = (5, 10, 15, 23, 13, 29)
for nombre in liste:
    print('Le nombre est ', nombre)

print("\n")
for lettre in 'Hello World':
    print(lettre)

print("\n")
for i, l in enumerate('Hello World'):
    print(i, l)

print("\n")
for mot in 'Hello World'.split():
    print(mot)

print("\n")

for i in "Hello World":
    print(i, end='')

print("\n")

for t in enumerate('Hello World'):
    print(t[0], t[1])