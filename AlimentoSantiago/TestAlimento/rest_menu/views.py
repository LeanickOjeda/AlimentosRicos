from tkinter import Menu
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import MenuSemana
from .serializers import MenuSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_menu(request):
    """
    Lista todos los Menu
    """
    if request.method == 'GET':
        menu = MenuSemana.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
