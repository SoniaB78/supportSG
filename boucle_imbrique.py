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

def main():
    pass



s = "analphabète"
l = enumerate(s)
print(l) #<enumerate object at 0x0000029E59B556C0> --> emplacement de stockage

l = [(0, 'a'), (1, 'n'), (2, 'a'), (3, 'l'), (4, 'p'), (5, 'h'), (6, 'a'), (7, 'b'), (8, 'a'), (9, 't'), (10, 'a')]
print(l)

for i in range(0, 10): #on va faire 10 tours pour les 10 tables
    i+=1 # rajoute une itération
    print("TABLE DE ", i, "\n")
    for j in range(0, 10):
        j+=1 # rajoute une itération
        print (i, "*", j, "=", i*j) #utilise le i pour multiplier le nbr
    print("\n")


def table_input():
    ''' DOCSTRING
    Fonction qui sert obtenir une table de multiplication à parti d'un prompt

    Parameters:
    choix : input ->string
    table : int(choix)

    Returns:
    print(string=numero de table)
    table * (de 0 à 10) = résultat
    x 10

    '''

    choix = input("Veuillez entrer la table de multiplication que vous souhaitez voir")
    table = int(choix)
    print("Table demandée", table)

    for i in range(0, 10): #on va faire 10 tours pour les 10 tables

        for j in range(0, 10):
            j+=1 # rajoute une itération
            print( j, "*", table, "=", table*j)
        break #arrête le script

    print("\n")


if __name__ == '__main__':
    #main()
    table_input()



