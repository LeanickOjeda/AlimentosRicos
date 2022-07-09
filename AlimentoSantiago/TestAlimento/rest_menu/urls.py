from django.urls import path
from rest_menu.views import lista_menu

urlpatterns = [
    path('lista_menu', lista_menu, name="lista_menu")
]