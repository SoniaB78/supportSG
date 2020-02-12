from django.urls import path

from . import views


urlpatterns = [ path('', views.teacherpage, name='teacherpage')]
