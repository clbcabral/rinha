from django.shortcuts import render, reverse
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from core.serializers import PessoaSerializer
from core.models import Pessoa
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
import json

# Create your views here.


@api_view(['GET', 'POST'])
def pessoas(request):
    
    if request.method == 'GET':
        term = request.query_params.get('t', None)
        if not term:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset = Pessoa.objects.annotate(search=SearchVector('apelido', 'nome', 'stack')).filter(search=term)
        serializer = PessoaSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['id']
            cache.set(id, serializer.data)
            headers = {'Location': reverse('recuperar-pessoa', args=[id])}
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recuperar_pessoa(request, pk):
    if request.method == 'GET':
        pessoa = cache.get(pk)
        if pessoa:
            return Response(pessoa)
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)


def contar_pessoas(request):
    return HttpResponse(Pessoa.objects.count())