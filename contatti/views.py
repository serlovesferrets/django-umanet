from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Contact

from contatti.forms import ContattoForm

from django.shortcuts import get_object_or_404, redirect

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required


def index(request: HttpRequest) -> HttpResponse:
    form = ContattoForm()
    context = {"form": form}
    return render(request, "contatti_contattaci.html", context)


def contatti(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContattoForm(request.POST)

        if form.is_valid():
            print("Form valido")
            print(f"Nome:\t\t{form.cleaned_data['first_name']}")
            print(f"Cognome:\t\t{form.cleaned_data['last_name']}")
            print(f"Email:\t\t{form.cleaned_data['email']}")
            print(f"Contenuti:\t\t{form.cleaned_data['contents']}")

            print("Salvataggio nel database")
            new_contact = form.save()
            print(f"New post: {new_contact}")

            return HttpResponse("<h1>risposta ricevuta</h1>")
    else:
        form = ContattoForm()

    context = {"form": form}
    return render(request, "contatti_contattaci.html", context)


def lista(request: HttpRequest) -> HttpResponse:
    context = {"contacts": Contact.objects.all()}
    return render(request, "contatti_lista.html", context)


@login_required(login_url="/accounts/login")
def modifica_contatto(request: HttpRequest, pk) -> HttpResponse:
    contatto = get_object_or_404(Contact, id=pk)

    if request.method == "GET":
        form = ContattoForm(instance=contatto)
    if request.method == "POST":
        form = ContattoForm(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect("contatti:lista")

    context = {"form": form, "contatto": contatto}
    return render(request, "modifica_contatto.html", context)


@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request: HttpRequest, pk) -> HttpResponse:
    contatto = get_object_or_404(Contact, id=pk)
    if request.method == "POST":
        contatto.delete()
        return redirect("contatti:lista")
    context = {"contatto": contatto}

    return render(request, "elimina_contatot.html", context)
