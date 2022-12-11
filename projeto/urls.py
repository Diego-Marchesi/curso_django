"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path


# HHTP REQUEST
def Home(request):
    return HttpResponse("HOME")
    # RETORNA HTTP RESPONSE


def Sobre(request):
    return HttpResponse("SOBRE")
    # RETORNA HTTP RESPONSE


def Contato(request):
    return HttpResponse("CONTATO")
    # RETORNA HTTP RESPONSE


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),  # HOME
    path('sobre/', Sobre),  # /sobre/
    path('contato/', Contato)  # /contato/
]
