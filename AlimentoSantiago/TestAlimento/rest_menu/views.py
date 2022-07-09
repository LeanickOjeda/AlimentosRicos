
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.forms import MenuForm
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
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_menu(request, id):
    try:
        menu = MenuSemana.objects.get(nrocatalogo=id)
    except MenuSemana.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
