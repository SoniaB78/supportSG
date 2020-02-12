from random import randint

class Pendu:

    def __init__(self):
        self.nbDeCoupsRestants = 7
        self.lettreTappees = []
        self.motAAfficher = []

    def creationListeDeMots(self,theme):
        "Création de la liste des mots en fonction du theme en attribut"
        self.affichageComplet
        self.listeDeMots = []

        if theme == "chiens":
            fichier = ".\\chiens\\index.csv"
        elif theme == "pays":
            fichier = ".\\pays\\index.csv"
        elif theme == "instruments":
            fichier = ".\\instruments\\index.csv"
        elif theme == "fruits":
            fichier = ".\\fruits\\index.csv"
        with open(fichier, encoding='utf-8') as f :
            for ligne in f:
                ligne_recuperee = f.readline()
                ligne_coupee = ligne_recuperee.split(";")
                print(ligne_coupee)
                mot = ligne_coupee[0]
                #image = ligne_coupee[1]
                #lien  = ligne_coupee[2]
                self.listeDeMots.append(mot)
        print(self.listeDeMots)

    def selectionMot(self):
        "Tire un mot au hasard dans la liste listeDeMots"
        self.motATrouver = self.listeDeMots[randint(0,len(self.listeDeMots)-1)]
        return self.motATrouver

    def lettreJoueePresente(self,lettreJouee):
        "Vérifie si la lettre est présente dans le mot"
        self.lettreTappees.append(lettreJouee)
        if lettreJouee in self.motATrouver:
            return True
        else:
            self.nbDeCoupsRestants -= 1
            return False

    def partiePerdue(self):
        "Vérifie si perdu"
        if self.nbDeCoupsRestants <= 0:
            return True
        else:
            return False

    def partieGagnee(self):
        "Vérifie si gagné"
        if "-" in self.motAAfficher:
            return False
        else:
            return True

    def affichageMot(self):
        "Crée le mot a afficher avec des '-' si la lettre n'a pas été tentée"
        self.motAAfficher = []
        for lettreMot in self.motATrouver:
            if lettreMot in self.lettreTappees:
                self.motAAfficher.append(lettreMot)
            else:
                self.motAAfficher.append("-")
        return self.motAAfficher

    def affichageComplet(self):
        print("Il reste",self.nbDeCoupsRestants,"coups")
        print("Lettre jouées :",self.lettreTappees)
        print(self.affichageMot())

##  Programme Principal

#   Initialisation programme
jeu = Pendu()
choixTheme = input("Theme ? (pays,chiens,instruments,fruits")
jeu.creationListeDeMots(choixTheme)
jeu.selectionMot()
print(jeu.motATrouver)
jeu.affichageComplet()

##  Boucle de jeu
while not jeu.partiePerdue() and not jeu.partieGagnee():
    "La boucle continue tant que je n'ai NI gagné, NI perdu"
    print("--------------------------")
    lettreATester = input("Quelle lettre ?").upper() #Demande de rentrer une lettre et la pousse en majuscule
    jeu.lettreJoueePresente(lettreATester)
    jeu.affichageComplet()

    #Si gagné ou perdu
    if jeu.partiePerdue() : print("PERDU !!!!!!!!!")
    if jeu.partieGagnee() : print("GAGNE !!!!!!!!!")