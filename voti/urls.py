from django.urls import path
from . import views

app_name = "voti"

urlpatterns = [
    path("", views.subjects_list, name="vista_1"),
    path("vista_2", views.student_grades, name="vista_2"),
    path("vista_3", views.student_averages, name="vista_3"),
    path("vista_4", views.max_and_min_grades, name="vista_4"),
]
