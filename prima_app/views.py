from django.shortcuts import render

def homepage(request):
    return render(request, "prima_app/homepage.html")

def welcome(request):
    return render(request, "prima_app/welcome.html")

def lista(request):
    return render(request, "prima_app/lista.html")

def variabili(request):
    context = {
        "var1": "Valore 1",
        "var2": "Valore 2",
        "var3": "Valore 3"
    }

    return render(request, "prima_app/variabili.html", context)

def index(request):
    return render(request, "prima_app/index.html")
