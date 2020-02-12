from django.shortcuts import render

from django.http import HttpResponse

def coursepage(request):
    contenu = """
                <h1> 
                   Page de cours
                </h1>

                <em>
                    Je me touve dans l'app course page ==> views.py
                </em>

                <hr>

                <table>
                    <thead>
                        <tr>
                            <th colspan="2">course name</th>
                            <th>classroom</th>
                            <th>teacher</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td colspan="2">fomation python</td>
                            <td>CDR</td>
                            <td>Gilles Véronie</td>
                        </tr>

                    </tbody>
                </table>
    """
    return HttpResponse(contenu)