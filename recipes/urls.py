from django.urls import path

from recipes.views import Contato, Home, Sobre

urlpatterns = [
    path('', Home),  # HOME
    path('sobre/', Sobre),  # /sobre/
    path('contato/', Contato)  # /contato/
]
