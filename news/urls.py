from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="homeview"),
    path("articoli/<int:pk>", views.article_detail, name="articolodettaglio"),
    path("lista_articoli", views.list_articles, name="articolodettaglio"),
    path("lista_articoli/<int:pk>", views.list_articles, name="articolodettaglio"),
]
