from rest_framework import serializers

from landing.models import Universo, Heroi, Habilidade, Arq_vilao


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('__all__')

class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroi
        fields =('nome', 'fraqueza', 'universo')

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model  =Habilidade
        fields = ('__all__')

class Arq_vilaoSerializer(serializers.ModelSerializer):
    hab_vilao = HabilidadeSerializer(many=True)
    class Meta:
        model = Arq_vilao
        fields =('__all__')
