"""
URL configuration for primo_progetto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from primo_progetto.views import index_root, chi_siamo

urlpatterns = [
    path("", index_root),
    path("chi_siamo", chi_siamo),
    path("admin/", admin.site.urls),
    path("prima_app/", include("prima_app.urls")),
    path("seconda_app/", include("seconda_app.urls")),
    path("news/", include("news.urls")),
    path("voti/", include("voti.urls")),
    path("corsi_formazione/", include("corsi_formazione.urls")),
    path("contatti/", include("contatti.urls"))
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
