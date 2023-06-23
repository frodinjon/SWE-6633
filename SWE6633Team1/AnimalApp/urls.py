#from django.conf.urls import path
from django.urls import path, re_path
from AnimalApp import views

urlpatterns = [
    re_path(r'^animal/$', views.animalApi),
    re_path(r'^animal/([0-9]+)$', views.animalApi)
]   