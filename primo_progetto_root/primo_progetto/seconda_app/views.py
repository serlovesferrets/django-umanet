import datetime
from django.shortcuts import render

def es_if(request):
    context = {
        "var1": 200,
        "var2": 200,
        "var3": 300
    }
    return render(request, "seconda_app/es_if.html", context)

def es_for(request):
    context = {
        "list1": [1, datetime.date(2019, 7, 16), "don't give up"],
        "list2": [1, datetime.date(2019, 7, 16), "don't give up"],
        "my_dict": {
            "chiave1" : "Valore1",
            "chiave2" : "Valore2"
        }
    }
    return render(request, "seconda_app/es_for.html", context)
