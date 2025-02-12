from datetime import date

from django.db.models import Max, Min, Sum
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from corsi_formazione.models import Course


def index(request: HttpRequest):
    return render(request, "corsi_base.html")


def view_a(request: HttpRequest):
    courses = Course.objects.all().order_by("date_start")
    context = {"courses": courses}
    return render(request, "view_a.html", context=context)


def view_b(request: HttpRequest):
    courses = Course.objects.all().order_by("date_start")
    context = {"courses": courses}
    return render(request, "view_b.html", context=context)


def view_b_detail(request: HttpRequest, id: int):
    course = get_object_or_404(Course, pk=id)
    context = {"course": course}
    return render(request, "view_b_detail.html", context=context)


def view_c(request: HttpRequest):
    courses = Course.objects.filter(date_start__gt=date(year=2025, month=5, day=1))
    context = {"courses": courses}
    return render(request, "view_c.html", context=context)


def view_d(request: HttpRequest):
    courses = Course.objects.filter(available_seats__lt=20)
    context = {"courses": courses}
    return render(request, "view_d.html", context=context)


def view_e(request: HttpRequest):
    courses = Course.objects.filter(date_end__lt=date(year=2025, month=4, day=30))
    context = {"courses": courses}
    return render(request, "view_e.html", context=context)


def view_f(request: HttpRequest):
    seats_data = Course.objects.all().aggregate(
        total_seats=Sum("available_seats"),
        most_seats=Max("available_seats"),
        least_seats=Min("available_seats"),
    )

    most_seats = (
        Course.objects.filter(available_seats=seats_data["most_seats"]).first()
        or "Nessun corso trovato!"
    )
    least_seats = (
        Course.objects.filter(available_seats=seats_data["least_seats"]).first()
        or "Nessun corso trovato!"
    )

    context = {
        "most_seats": most_seats,
        "least_seats": least_seats,
        "total_seats": seats_data["total_seats"],
    }

    return render(request, "view_f.html", context=context)
