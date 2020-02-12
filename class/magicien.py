#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#

# Created:     17/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# CLASSE MERE
# Elle ne contient que l'attibut nom
class Personnage(object):
    def __init__(self):
        self.nom = ""


# CLASSE FILLE
# Elle contient  l'attibut race pv pvMax (pv = point de vie)
class Race(Personnage):
    #class fille
    def __init__(self):
        Personnage.__init__(self)
        self.race = ""
        self.pv = 0
        self.pvMax = 0



# CLASSE PETITE FILLE
# Elle contient  l'attibut classe pm pmMax (pm = point de magie)
# Et la méthode magie qui lance un sort
class Classe (Race):
    #classe petite fille
    def __init__(self):
        Race.__init__(self)
        self.classe = "magicien" # Cest attribut n'est pas vide parce que tous mes personnages créés seront magicien
        self.pm = 0
        self.pmMax = 0

    def afficheCarac(self):
        """affichage des attributs avec formatage %s pour string %i pour integer:
         °~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°
            Igor est humain un magicien:
 	           POINTS DE VIE : 30
 	           POINTS DE MAGIE: 20

         °~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°
        """
        print(" °~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°" )
        print(" %s est %s un %s:\n \t POINTS DE VIE : %i \n \t POINTS DE MAGIE: %i  \n "%(self.nom, self.race, self.classe, self.pvMax, self.pmMax))
        print("°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°")

    def magie(self, autre):
        # à l'appel de la méthode ne pas oublié self.nomDeLaMethode(autre)
        # self personnage instancié qui lance le sort, et autre le personnage sur qui on lance le sort
        if self.pm  < 0:
            autre.pv += self.pm
        else:
            autre.pv -= self.pm


"""
---------------------------------PROGAMME PRINCIPAL-----------------------------
"""
##INSTANCIATION
perso1 = Classe()
##DEFINITION DES ATTIBUTS
perso1.nom = "Igor"
perso1.race = "humain"
perso1.pv = 30
perso1.pvMax = 30
perso1.pm = 20
perso1.pmMax = 20
#AFFICHAGEAVEC LA METHODE afficheCarac
print(perso1.afficheCarac())

##INSTANCIATION
perso2 = Classe()
##DEFINITION DES ATTIBUTS
perso2.nom = "Charlyne"
perso2.race = "elfe"
perso2.pv = 25
perso2.pvMax = 25
perso2.pm = 30
perso2.pmMax = 30
#AFFICHAGEAVEC LA METHODE afficheCarac
print(perso2.afficheCarac())

#UTILISATION DE LA METHODE "magie"
perso1.magie(perso2)
print("perso1 à lancé un sort sur perso2")
print("Nombre de point de vie restant à perso2", perso2.pv)

