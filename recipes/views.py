from django.shortcuts import render


# HHTP REQUEST
def Home(request):
    return render(request, 'recipes/home.html')
