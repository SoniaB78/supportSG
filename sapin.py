#-------------------------------------------------------------------------------
# Name:        sapin
# Purpose:
#
# Author:      Administrateur
#
# Created:     10/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Nombre de lignes constituant le sapin
nbre_ligne = int(input("Veuillez entre le nombre de rangs"))
# Nombre de "blancs" à insérer avant le ^
padSize=nbre_ligne - 1
# Position actuelle en lignes dans le dessin du sapin
num_ligne = 0
space=' '
def sapin(char,Lines):

    numChars = lambda h : h == 1 and 1 or h + ( h-1 )
    # fontion en ligne affectée à la variable
    #
    MaxTreeWidth = numChars(Lines)
    padSize = ( Lines -1)
    print
    for lineNumber in range(1,Lines + 1):
        print (space * (padSize), char * numChars(lineNumber),space * (padSize))
        #affiche ( espace fois nbLigne-1, '*' fois
        padSize -=1


def sapinv2():
    n=int(input())
    for i in range(n):
        print(f'{"*"*(i*2+1):^{2*n}}')
    print(' '*(n-1)+'#')


def sapinv3():
    n=10
    for i in range(n):
        if i < 5 : print(f'{"*"*(i*2+1):^{2*n}}')
        if i >= 5:print(f'{"*"*(i*2-3):^{2*n}}') and print(f'{"*"*(i*2+1):^{2*n}}')

    print(' '*(n-2)+'###')


def sapinv4():
    n=10
    for i in range(n):
        if i == 0: print(f'{"¤"*(i*2+1):^{2*n}}')
        if i > 0 and i < 5: print(f'{"*"*(i*2+1):^{2*n}}')
        if i == 5: print(f'{"*"*(i*2-3):^{2*n}}')#rajouter @ au début et à la fin
        if i >= 6: print(f'{"*"*(i*2-3):^{2*n}}') and print(f'{"*"*(i*2+1):^{2*n}}')

    print('###'.center(20))
#possibilité de rajouter un triangle


def sapinv5():
    n=5#int(input())
    star = "¤"
    print(star.center(20))
    star = "*"
    for i in range(n):
        star +="***"
        print(star.center(20))
        if i%2 == 0: print("@{}@".format(star).center(20))
    print('###'.center(20))


#https://openclassrooms.com/forum/sujet/sapin-de-noel-python-1
def sapin6():
    phrase = "Joyeux Noël et Bonne Année 2020 !!!"
    phrase = phrase.replace(" ","") # transfome les espaces en rien ""
    liste_mots = []

    i = 1
    while i < len(phrase):#boucle sur la longueur de la phrase
        section, phrase = phrase[:i], phrase[i:] #je coupe jusqu'a i que je stocke dans 'section' et en même temps met a jour phrase
        liste_mots.append(section) # je stocke mot dans la liste
        i += 1

    size = len(liste_mots[-1]) + 1

    if len(phrase)%2 == 0:
        for paquet in range(0, len(phrase), 2):# je génère des indices de 2 en 2 jusqu'à la fin
            liste_mots.append( phrase[paquet:paquet+2])#j'ajoute les paquets de 2 à la liste de mots

    else:
        for paquet in range(0, len(phrase), 1):# je génère des indices de 1 en 1 jusqu'à la fin
            liste_mots.append( phrase[paquet:paquet+1])#j'ajoute les paquets de 1 à la liste de mots


    for mot in liste_mots: # on affiche l'arbre
        print(" " * (len(mot) % 2) + " ".join(mot.center(size)))



if __name__ == "__main__":
    #sapin('*',nbre_ligne)
    #sapinv2()
    #sapinv3()
    #sapinv4()
    #sapinv5()
    sapin6()

    #pass

'''
print('il manque le pied!!, mais bon travail.')
print('merci')
'''

