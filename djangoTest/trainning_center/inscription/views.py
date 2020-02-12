from django.shortcuts import render

from django.http import HttpResponse

def inscriptionpage(request):
    contenu = """
                <h1> 
                    Page inscription 
                </h1>

                <em>
                    Je me touve dans l'app inscription page ==> views.py
                </em>

                <hr>

                <form action="" >
                    <div>
                        <label >Nom :</label>
                        <input type="text" id="name" name="nom">
                    </div>

                    <div>
                        <label >Prénom :</label>
                        <input name="prenom" name="prenom">
                    </div>

                    <div>
                        <label >e-mail :</label>
                        <input type="email"  name="mail">
                    </div>
                </form>
    """
    return HttpResponse(contenu)