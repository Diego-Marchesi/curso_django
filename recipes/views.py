from django.http import HttpResponse
from django.shortcuts import render


# HHTP REQUEST
def Home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse("CONTATO 1")
    # RETORNA HTTP RESPONSE

# Create your views here.
