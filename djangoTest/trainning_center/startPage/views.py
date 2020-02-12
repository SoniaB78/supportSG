from django.shortcuts import render
from django.http import HttpResponse

def thestartingpage(request):
    contenu = """
                <section>
                <h2>
                    This is a training center sessions management
                </h2>
    
                <h3>
                    From the interface, you can : 
                </h3>
    
                <p>
                    Make operations as list, add, suppr, modify on students :
                    And so on for teacher, session, classrooms.
                </p>
    
                <ul class="square_list">
                    <li>list</li>
                    <li>add</li>
                    <li>suppr</li>
                    <li>modify</li>
                </ul>
            </section>
    
            <section>
                <hr>
    
                <p>For app administration, if you are allowed</p>
    
                <ul>
                    <li>
                        <a href="/admin">Main interface</a>
                    </li>
    
                    <li>
                        <a href="www.google.fr">If help needed</a>
                    </li>
    
                    <li>
                        <a href="wwww.stackoverflow.org">If help still needed</a>
                    </li>
                </ul>
            </section>
    """
    return HttpResponse(contenu)