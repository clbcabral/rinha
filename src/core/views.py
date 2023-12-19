from django.shortcuts import render, reverse
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from core.serializers import PessoaSerializer
from core.models import Pessoa
from rest_framework import viewsets
from rest_framework import generics
import json

# Create your views here.

class CriarPessoaView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def get_queryset(self):
        queryset = Pessoa.objects.all()
        term = self.request.query_params.get('t', None)
        if term is not None:
            queryset = Pessoa.objects.annotate(search=SearchVector('apelido', 'nome', 'stack')).filter(search=term)
        return queryset

    def get_success_headers(self, data):
        return {'Location': reverse('recuperar-pessoa', args=[data['id']])}

class RecuperarPessoaView(generics.RetrieveAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


def contar_pessoas(request):
    return HttpResponse(Pessoa.objects.count())