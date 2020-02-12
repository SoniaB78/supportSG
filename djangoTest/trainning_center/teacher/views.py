from django.shortcuts import render

from django.http import HttpResponse

def teacherpage(request):
    contenu = """
                <h1> 
                    Page teacher
                </h1>

                <em>
                    Je me touve dans l'app teacher page ==> views.py
                </em>

                <hr>

                    <img src="#" alt="Ici une photo de Gille Véronie">
                <p> 
                    nom: Véronie
                </p>
                <p> 
                    prénom: Gilles
                </p>
    """
    return HttpResponse(contenu)