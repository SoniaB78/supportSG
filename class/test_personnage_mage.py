#-------------------------------------------------------------------------------
# Name:        Magicien
# Purpose:
#
# Author:      Administrateur
#

# Created:     17/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Personnage:
    def __init__ (self):
        self.nom = ""
        self.pv = 0
        self.pvMax = 0
        self.force = 0
        self.endurance = 0
        self.rapidite = 0
        self.intelligence = 0

    def estMort(self):
        if (self.pv > 0):
            return False
        else:
            return True

    def afficheEtat(self):
        if (self.estMort() == False):
            print(self.nom, "à", self.pv, "points de vie.")
        else:
            print(self.nom, "est mort !")

    def afficheCarac(self):
        print(" °~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°" )
        print(" %s est un %s %s:\n \t FORCE : %i \n \t ENDURANCE: %i \n  \t RAPIDITE: %i \n \t INTELLIGENCE: %i \n "%(self.nom, self.race, self.classe, self.force, self.endurance, self.rapidite, self.intelligence))
        print("°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°")

    def perdVie(self, nbrPvPerdu):
        if (nbrPvPerdu >= self.pv):
            print("L'ennemi vous attaque !", self.nom, "subit une attaque mortelle !" )
            self.pv = 0
        else:
            print("L'ennemi vous attaque !", self.nom, "perd:", nbrPvPerdu, "points de vie !" )
            self.pv -= nbrPvPerdu

    def gagneVie(self, nbrPvGagne):
        if (self.estMort() != True):
            pvTmp = nbrPvGagne + self.pv
            if( pvTmp <= self.pvMax):
                self.pv += nbrPvGagne
                print(self.nom, "a été soigné, ses points de vie s'élèvent à:", self.pv, "points de vie.")
            elif (self.pv == self.pvMax):
                print(self.nom, "utilise une potion de soin mais", self.nom, "est deja à son maximum de point de vie.")
        else:
            print(self.nom, "ne peut être soigné car il est mort.")

    def attaque(self, ennemi):
        if (self.estMort() == False):
            if (ennemi.esquive(self) == False):
                self.degats = round(0.6 * self.force)
                ennemi.pv -= self.degats
                print("Vous infligez:", self.degats, "points de dégat à", ennemi.nom)
        else:
            print(self.nom, "ne peut attaquer car il/elle est mort(e).")

    def soigne(self, allie, nbrPvSoigne):
        if (self.estMort() == False and allie.estMort() == False):
            pvTmp = nbrPvSoigne + allie.pv
            if( pvTmp <= allie.pvMax):
                allie.pv += nbrPvSoigne
                print(self.nom, "soigne", allie.nom, ",", allie.nom, "récupère", nbrPvSoigne, ", il est à:", allie.pv, "points de vie.")

            elif (allie.pv == allie.pvMax):
                print(self.nom, "utilise un sort de soin mais", allie.nom, "est deja à son maximum de point de vie.")

            else:
                allie.pv += allie.pvMax
                print(allie.nom, "retoune à son maximum de point de vie:", allie.pvMax)


        elif (allie.estMort() == True):
            print(self.nom, "ne peut pas soigner", allie.nom, "car il est mort !")

        else:
            print(allie.nom, "ne peut pas être soigné car", self.nom, "est mort !")

    def esquive (self, ennemi):
        if (self.estMort() == False and ennemi.estMort() == False):
            if (self.rapidite > ennemi.rapidite):
                print(self.nom, "esquive l'attaque de", ennemi.nom)
                return True
                print("La rapidité de ",self.nom ,"est de:", self.rapidite,"contre",ennemi.nom ,"pour", ennemi.rapidite)
            else:
                print(self.nom, "a raté son esquive.")
                return False
        elif ( self.estMort() == True):
            print(self.nom, "ne peut esquiver l'attaque de", ennemi.nom, "car il est mort.")
        else:
            print(self.nom, "ne peut esquiver d'attaque car il est mort !")

    def mouvement(self, deplacement):#passer la direction : rester ou fuir
        if (self.estMort() != True):
            mouvement = input=("Voulez vous rester ou fuir")
            if (deplacement == "rester"):
                print(self.nom, "tient la position.")
            elif (deplacement == "fuir"):
                print(self.nom, "s'enfuit à toute jambes.")

class Magicien(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.classe = "magicien"
        self.race = ""
        self.pm = 0
        self.pmMax = 0

        def magie(self, autre):
            if self.pm  < 0:
                autre.pv += self.pm
            else:
                autre.pv -= self.pm

##INSTANCIATION
perso2 = Magicien()
##DEFINITION DES ATTIBUTS
perso2.nom = "Charlyne"
perso2.race = "elfe"
perso2.pv = 25
perso2.pvMax = 25
perso2.pm = 30
perso2.pmMax = 30
perso2.force = 15
perso2.endurance = 15
perso2.rapidite = 30
perso2.intelligence = 25
perso2.classe = "magicien"
perso2.race = "Elfe"
perso2.pm = 25
perso2.pmMax = 25
#AFFICHAGE
print(perso2.afficheCarac())



