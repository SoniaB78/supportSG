#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     17/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def dimension(tab1): # Pour afficher les dimensions d'un matice
    maxi, maxj = 0, 0
    for k in tab1:
        maxi = max(maxi, k[0])
        maxj = max(maxj, k[1])
    return maxi + 1, maxj + 1

def veriflong(tab1, tab2):
    if len(tab1) == len(tab2) and len(tab1[0]) == len(tab2[0]):
    # vérifie que la longueur des colonnes et des lignes sont égales dans les deux tableaux
        return True
    else:
        return False


def verifcar(tab1, tab2):
    if len(tab1[0]) == len(tab2):
    # vérifie que la table est carrée couplée à veriflong
        return True
    else:
        return False


def addition(tab1, tab2):
    tab3 =[]
    if veriflong(tab1, tab2) == True and verifcar(tab1, tab2) == True:
    #Si les deux autres fonctions renvoient true parcours les tableaux
        for i in range(len(tab1)):
            tmp = [] #obligation de stocker dans une var temp pour l'assigner à tab3
            # Pourquoi??
            for j in range(len(tab2)):
                tmp.append(tab1[i][j] + tab2[i][j])
                # Parcours tab1 et tab2 par indice
            tab3.append(tmp)
        print(tab3)
    else:
        print("NOPE")


def multiplication(tab1, tab2):
    tab3 =[]
    if veriflong(tab1, tab2) == True and verifcar(tab1, tab2) == True:
        #Si les deux autres fonctions renvoient true parcours les tableaux
        for i in range(len(tab1)):
            tmp = [] #obligation de stocker dans une var temp pour l'assigner à tab3
            # Pourquoi??
            for j in range(len(tab2[0])):# Troisième boucle
                total =0
                for k in range(len(tab2)):
                    total +=(tab1[i][k] * tab2[k][j])
                    tmp.append(total)
                print(total)
            tab3.append(tmp)
        print(tab3)
    else:
        print("NOPE")

def transposition(tabbase):
    tab4 = []
    for i in range(len(tabbase[0])):# hein?
        tmp = []#obligation de stocker dans une var temp pour l'assigner à tab3
        for j in range(len(tabbase)):
            tmp.append(tabbase[j][i])# inverse les indices de chaque valeur
        tab4.append(tmp)
#tabbase= [[19, 22, 1], [43, 50, 2]]

def determinant(tab1):
    tmp1 = 1
    tmp2=1
    total= 0
    for i in range(len(tab1)):#parcourt les lignes
        for j in range (len(tab1)): #Parcourt les colonnes
            if i == j:# si les indices sont égaux 00 ou 11
                tmp1 *= tab1[i][j]#mémorise la valeur pour le multiplier avec la prochaine
            else:
                tmp2 *= tab1[i][j]#mémorise la valeur pour le multiplier avec la prochaine

    total=tmp1-tmp2 #pour calculer le determinant on fait moins entre les deux produits
    return total


def exo():
    liste = [1, 2, 3, 4]# méthode Khalid/ Yusuf
    long = len(liste)
    for i in range(12):
        for j in range(0, long):
            print(liste[0])
        for k in range(1,4):
            print(liste[k])
"""
    for i in range(1, 13): # ma tembouille avec [[ ]]
        for j in range(0, 5):
            for k in range(1,4):
                if j == 0:
                    print("1")
            if j != 0:
                print(j)
"""

def inversionMatrice(tab1):
    inv = []
    long = len(tab1)
    #première partie du calcul
    #récupération du déterminant de tab1
    det = determinant(tab1)
    #process : inversion des valeurs a-> c, c-> a et b-> -b, d-> -d
    tab1[0][0], tab1[1][1] = tab1[1][1], tab1[0][0]
    tab1[1][0] *= -1
    tab1[0][1] *= -1
    #det qui devient scalaire de l'adjointe transposée de A
    for i in range(long):
        tmp =[]
        for j in range(long):
            tmp.append(tab1[i][j]/det)
        inv.append(tmp)
    return [inv, det, tab1]






if __name__ == '__main__':
    tab1 = [[1, 2],[3, 4]]
    tab2 = [[5, 6],[7, 8]]
    #dimension(tab1)
    #addition(tab1, tab2)
    #multiplication(tab1, tab2)
    transposition(tab1)
    determinant(tab1)
    #exo()
    list=inversionMatrice(tab1)
    print("La matrice inversée de A (soit A-1) = 1/det: 1/", list[1], " * matrice adjointe transposée :", list[2], ":", list[0])