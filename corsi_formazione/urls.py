from django.urls import path
from . import views

app_name = "corsi_formazione"

urlpatterns = [
    path("", views.index, name="index"),
    path("view_a", views.view_a, name="view_a"),
    path("view_b", views.view_b, name="view_b"),
    path("view_b_detail/<int:id>", views.view_b_detail, name="view_b_detail"),
    path("view_c", views.view_c, name="view_c"),
    path("view_d", views.view_d, name="view_d"),
    path("view_e", views.view_e, name="view_e"),
    path("view_f", views.view_f, name="view_f"),
]
