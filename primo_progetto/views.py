from django.shortcuts import render

def index_root(request):
    return render(request, "index_root.html")

def chi_siamo(request):
    return render(request, "chi_siamo.html")
