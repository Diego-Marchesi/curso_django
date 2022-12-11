from django.http import HttpResponse
from django.shortcuts import render


# HHTP REQUEST
def Home(request):
    return render(request, 'recipes/home.html')


def Sobre(request):
    return HttpResponse("SOBRE 1")
    # RETORNA HTTP RESPONSE


def Contato(request):
    return HttpResponse("CONTATO 1")
    # RETORNA HTTP RESPONSE

# Create your views here.
