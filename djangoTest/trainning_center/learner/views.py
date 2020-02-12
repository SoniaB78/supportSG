from django.shortcuts import render

from django.http import HttpResponse

def learnerpage(request):
    contenu = """
                <h1> 
                    Learner page
                </h1>

                <em>
                    Je me touve dans l'app leaner page ==> views.py
                </em>

                <hr>

                <table>
                    <thead>
                        <tr>
                            <th colspan="2">mail</th>
                            <th>nom</th>
                            <th>prénom</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td colspan="2">your@mail</td>
                            <td>votre nom</td>
                            <td>votre prénom</td>
                        </tr>

                    </tbody>
                </table>
    """
    return HttpResponse(contenu)