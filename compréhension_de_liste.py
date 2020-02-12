#-------------------------------------------------------------------------------
# Name:        boucles truc
# Purpose:
#
# Author:      Administrateur
#
# Created:     11/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

liste_initiale = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def main():
    liste2 = []
    for i in liste_initiale:
        liste2.append(i*2)
    print("La liste 2 est :", liste2)

def main2():
    liste2 = [n*2 for i in liste_initiale]
    print("La liste 2 en compréhension de liste est :", liste2)

def main3():
    liste_pair = []
    for i in liste_initiale:
        if i % 2 == 0:
            liste_pair.append(i*2)
    print("La liste pair est :", liste_pair)

def main4():
    liste_pair = [i*2 for i in liste_initiale if i % 2 == 0]
    print("La liste pair est en compréhension de liste :", liste_pair)

def main5():
    nouvelle_liste = []
    for i in liste_initiale:
        if i % 2 == 0:
            nouvelle_liste.append(i*2)
        else:
            nouvelle_liste.append(i*3)
    print("La nouvelle liste est :", nouvelle_liste)

def main6():
    nouvelle_liste = [i*2 if i % 2 ==0 else i*3 for i in liste_initiale]
    print("La nouvelle liste en compréhension de liste est :", nouvelle_liste)


liste_imbrique = [[0, "a"],[2,"b"],[3,"c"]]

def main7():
    nouvelle_liste = []
    for i in liste_imbrique:
        for j in i:
            nouvelle_liste.append(j*2)

    print(nouvelle_liste)

def main8():
    # la variable qu'on modifie = calcul, condition (if, else), for 1 for 2
    nouvelle_liste = [j*2 for i in liste_imbrique for j in i ]
    print(nouvelle_liste)

def main9():
    nouvelle_liste = [i*2 if type(i)==int else i*3 for j in liste_imbrique for i in j]
    print(nouvelle_liste)

def main10():
    nouvelle_liste = []
    for j in liste_imbrique:
         for i in j:
            if type(i)==int:
               nouvelle_liste.append(i*2)
            else:
                nouvelle_liste.append(i*3)
    print(nouvelle_liste)

def main11():
    prenom = "Gustave"
    liste_lettres = [lettre for lettre in prenom]
    print(liste_lettres)

def main12():
    prenom = "Gustave"
    liste_lettres = []
    for lettre in prenom:
        liste_lettres.append(lettre)
    print(liste_lettres)




if __name__ == '__main__':
    #main()
    #main2()
    #main3()
    #main4()
    #main5()
    #main6()
    #main7()
    #main8()
    #main9()
    #main10()
    main12()
