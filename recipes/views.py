from django.shortcuts import render

# import fake para criação altomatica e testes
from utils.recipes.factory import make_recipe

from .models import Recipe


# HHTP REQUEST
def Home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def Recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
