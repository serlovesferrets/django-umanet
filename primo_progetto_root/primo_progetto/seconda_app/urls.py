from django.urls import path 
from seconda_app.views import es_if, es_for

app_name = "seconda_app"

urlpatterns = [
    path("es_if", es_if, name="es_if"),
    path("es_for", es_for, name="es_for")
]
