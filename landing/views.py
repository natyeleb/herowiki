from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from landing.models import Heroi, Universo, Habilidade, Arq_vilao
from landing.serializers import HeroiSerializer, UniversoSerializer, HabilidadeSerializer, Arq_vilaoSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer

class UniversoViewSet(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer

class VilaoViewSet(viewsets.ModelViewSet):
    queryset = Arq_vilao.objects.all()
    serializer_class = Arq_vilaoSerializer