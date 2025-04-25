from django.urls import path
from . import views

app_name = "contatti"

urlpatterns = [
    path("contattaci", views.contatti, name="contattaci"),
    path("lista", views.lista, name="lista"),
    path("eliminacontatto/<int:pk>", views.elimina_contatto, name="elimina-contatto"),
    path("modificacontatto/<int:pk>", views.modifica_contatto, name="modifica-contatto"),
]
