from django.urls import path

from . import views


urlpatterns = [ path('', views.classroompage, name='classroompage')]
