#-------------------------------------------------------------------------------
# Name:        CHeritages
# Purpose:
#
# Author:      Sonia
#
# Created:     17/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
class Alphabet_majuscules(object):
    #class mere
    def __init__(self):
        #équivalent à une chaine de caractère reprenant tout l'alphabet avec la méthode upper()
        self.lettres_maj = string.ascii_uppercase

        """
            class Alphabet_majuscules(object):
            constuction d'un class mere comme une classe normale ordinaire

            self.lettres = sting.ascii_uppercase
            importation de la constante "sting.ascii_uppercase" du module "string" qui est l'alphabet en majuscules

        """

class Alphabet_minuscules(Alphabet_majuscules):
    #class fille
    def __init__(self):
        Alphabet_majuscules.__init__(self)
        self.lettres_min = self.lettres_maj.lower()

        """
            class Alphabet_minuscules(Alphabet_majuscules): en paamètre de la classe fille le nom de la classe mère
            alphabet_majuscules.__init__(self): dans le constructeur de la classe fille,
                importation du constructeur de la classe mère avec ses attibuts.
            En paramètre de la classe fille, le nom de la classe mère.
            Dans le constuteur de la classe fille, importation du constucteur de la classe mère avec ses attributs

        """

class Alphabet_tri (Alphabet_minuscules):
    #classe petite fille
    def __init__(self):
        Alphabet_minuscules.__init__(self)
        self.voyelles = []
        self.consonnes = []
        for lettre in self.lettres_min:
            if lettre in "aeiouy":
                self.voyelles.append(lettre)
            else:
                self.consonnes.append(lettre)

    def listes_vers_chaines(self):
        self.voyelles_chaine = "".join(self.voyelles)
        self.consonnes_chaine = "".join(self.consonnes)


alphabetM = Alphabet_majuscules()
alphabetm = Alphabet_minuscules()
alphabetTri = Alphabet_tri()

print(alphabetM.lettres_maj)#classe mère

print(alphabetm.lettres_maj)#classe fille
print(alphabetm.lettres_min)

print(alphabetTri.consonnes)# classe petite fille
print(alphabetTri.voyelles)
print(alphabetTri.listes_vers_chaines())



