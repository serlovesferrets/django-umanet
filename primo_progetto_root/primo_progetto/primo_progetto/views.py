from django.shortcuts import render

def index_root(request):
    return render(request, "primo_progetto/index_root.html")

def chi_siamo(request):
    return render(request, "primo_progetto/chi_siamo.html")
