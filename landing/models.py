from django.db import models

# Create your models here.

class Universo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Heroi(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name= 'Nome'
    )
    fraqueza = models.CharField(
        max_length=255,
        verbose_name= 'fraqueza'
    )
    universo= models.ForeignKey(Universo, on_delete=models.CASCADE)

class Habilidade(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    nivel_habilidade = models.IntegerField()

    hab_heroi = models.ManyToManyField(Heroi,related_name='habilidade')

class Arq_vilao(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    universo=models.ForeignKey(Universo,on_delete=models.CASCADE)
    heroi=models.ForeignKey(Heroi,on_delete=models.CASCADE)
    hab_vilao = models.ManyToManyField(Habilidade, related_name='Arq_vilao')

