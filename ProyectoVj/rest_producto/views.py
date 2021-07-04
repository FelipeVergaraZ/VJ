from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from videojuego.models import Mercancia

from .serializers import MercanciaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt

@api_view(['GET','POST'])



def lista_mercancia(request):

    if request.method == 'GET':

        mercancia = Mercancia.objects.all()

        serializer = MercanciaSerializer(mercancia, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)

        serializer = MercanciaSerializer(data=data)

        if(serializer.is_valid()):

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
