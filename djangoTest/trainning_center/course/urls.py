from django.urls import path

from . import views


urlpatterns = [ path('', views.coursepage, name='coursepage')]
