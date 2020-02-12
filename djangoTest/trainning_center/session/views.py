from django.shortcuts import render

from django.http import HttpResponse

def sessionpage(request):
    contenu = """
                <h1> 
                    Page session
                </h1>

                <em>
                    Je me touve dans l'app session page ==> views.py
                </em>

                <hr>
                
                <p>
                    NOM DE LA FORMATION SUIVIE : sdfgbn4123.
                </p>
    """
    return HttpResponse(contenu)