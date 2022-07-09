from unicodedata import name
from django.urls import path
from rest_menu.views import lista_menu, detalle_menu

urlpatterns = [
    path('lista_menu', lista_menu, name="lista_menu"),
    path('detalle_menu/<id>', detalle_menu, name="detalle_menu"),
]