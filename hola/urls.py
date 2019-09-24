from django.urls import path
from hola import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hola/<name>", views.hola_there, name="hola_there"),
]