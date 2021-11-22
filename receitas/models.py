from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.
class Receita(models.Model):
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=200)
    categoria =models.CharField(max_length=200)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

    def __str__(self):
        return self.nome_receita

class Skill (models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    percentage = models.PositiveIntegerField(default=100)