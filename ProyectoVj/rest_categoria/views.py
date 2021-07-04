from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from videojuego.models import Categoria
from rest_categoria.serializers import CategoriaSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])


def lista_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DETALLES DE LAS CATEGORIAS EN JSON (OBTENER, MODIFICAR Y BORRAR)
@api_view(['GET','PUT','DELETE'])
def detalle_categoria(request,id):
    try:
        categoria = Categoria.objects.get(ID_CATPROD=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if(categoria.delete()):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NOT_CONTENT)