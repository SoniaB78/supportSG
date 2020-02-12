from django.shortcuts import render
from django.http import HttpResponse

def classroompage(request):
    contenu = """
                <h1> 
                    Page classroom 
                </h1>

                <em>
                    Je me touve dans l'app classroom page ==> views.py
                </em>

                <hr>

                <p> 
                    bla bla bla les salles de cours...
                </p>
    """
    return HttpResponse(contenu)