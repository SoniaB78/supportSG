from django.shortcuts import render
import datetime

def layout(request):
    the_date = "{date:%Y-%m-%d}".format(date=datetime.datetime.today())
    the_time = "{time:%H-%M-%S}".format(time=datetime.datetime.now())
    prenom = "Sonia"
    dictionary = {"date":the_date, "time":the_time, "prenom":prenom}
    return render(request, "layout.html", dictionary)
