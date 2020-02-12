#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     20/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#------------------------------------------------------------------------------
class Voiture():
    def __init__(self):
        """Constucteur de notre classe"""
        self.nombre_roues = 4
        self.nombre_fauteils = 1
        self.moteur = False
        self.volant = True

    def start_moteur(self):
        self.moteur = True
        return self.moteur

    def stop_moteur(self):
        self.moteur = False
        return self.moteur

    def statut_moteur(self):
        return self.moteur


class Citroen():
    def __init__(self):
        self.type_suspension = "Hydractives"
        self.logo = "Chevrons"
        self.marque = "Citroën"


class BondBug(Voiture):
    def __init__(self):
        #Héritage de voiture
        Voiture.__init__(self)
        self.modele = "Bug"
        self.marque = "Bond"
        self.nombre_roues = 3
        self.nombre_fauteils = 2

    def start_moteur(self):
        #attention bien mettre le self sinon la surcharge ne se fera pas
        state = Voiture.start_moteur(self)
        print("Staus du moteur: %s" % (state))

    def stop_moteur(self):
        state = Voiture.stop_moteur(self)
        print("Staus du moteur: %s" % (state))

class CitroenDs(Voiture, Citroen):
        def __init__(self):
            Voiture.__init__(self)
            Citroen.__init__(self)
            self.modele = "DS de 1967"


if __name__ == "__main__":
    ma_voiture_basique = Voiture()

    print(ma_voiture_basique.statut_moteur())
    ma_voiture_basique.start_moteur()
    print(ma_voiture_basique.statut_moteur(), "\n")

    ma_citroen = Citroen()

    print("Ma citroen:", ma_citroen.type_suspension)
    print(ma_citroen.logo)
    print(ma_citroen.marque, "\n")

    ma_bug = BondBug()

    print("Ma bug:", ma_bug.nombre_fauteils)
    ma_bug.start_moteur()
    ma_bug.stop_moteur()

    ma_super_DS = CitroenDs()

    print("\n Ma super DS:", ma_super_DS.nombre_roues)
    print(ma_super_DS.logo)
    print(ma_super_DS.modele)
    print(ma_super_DS.type_suspension)
    ma_super_DS.start_moteur()
    print(ma_super_DS.marque, "\n")





"""
    ma_voiture1 = Voiture()

    print("Ma voiture:", ma_voiture1.nombre_roues)
    print(ma_voiture1.nombre_fauteils, "\n")


    class Citroen():
        def __init__(self):
            self.type_suspension = "Hydractives"
            self.logo = "Chevrons"
            self.marque = "Citroën"

    ma_citroen = Citroen()

    print("Ma citroen:", ma_citroen.type_suspension)
    print(ma_citroen.logo)
    print(ma_citroen.marque, "\n")





    class CitroenC4(Voiture, Citroen):
        def __init__(self):
            Voiture.__init__(self)
            Citroen.__init__(self)
            self.couleur = "rouge"
            self.conducteur = "Florent"

    sa_citroen = CitroenC4()

    print("Sa citröen:", sa_citroen.nombre_roues)
    print(sa_citroen.logo)
    print(sa_citroen.couleur, "\n")
"""
