from django.shortcuts import render

# import fake para criação altomatica e testes
from utils.recipes.factory import make_recipe


# HHTP REQUEST
def Home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def Recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
