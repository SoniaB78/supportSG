from django.urls import path

from . import views


urlpatterns = [ path('', views.thestartingpage, name='thestartingpage')]
