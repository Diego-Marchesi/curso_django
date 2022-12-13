from django.urls import path

from recipes.views import Home, contato, sobre

urlpatterns = [
    path('', Home),  # HOME
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato)  # /contato/
]
