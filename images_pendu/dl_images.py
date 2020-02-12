#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     19/12/2019
# Copyright:   (c) Administrateur 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup as bs
import wget

listeImages = []
listeFinale = []

#Url a récupérer
url = "https://wamiz.com/chiens/race-chien"

#Récupération du code source
r = requests.get(url)
source = r.text
print(source)
soup = bs(source, 'html.parser')


#Récupération des liens
for lien in soup.findAll("img","trigger"):

    coupe = str(lien)
    coupe = coupe.split("src=")
    image = coupe[-1].replace('/>',"")
    image = image.replace('"','')
    listeImages.append(image)


#Une ligne sur deux m'interesse
for i in range(len(listeImages)):
    if i % 2 == 1:
        listeFinale.append(listeImages[i])


#Récupération des images
for lien in listeFinale:

    wget.download(lien)
    print(lien)
