from unittest.util import _MAX_LENGTH
from django.db import models
from autor.models import Autor
from coorientador.models import Coorientador
from orientador.models import Orientador

# Create your models here.
class Monografia(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete = models.CASCADE)
    coorientador = models.ForeignKey(Coorientador, on_delete = models.CASCADE)
    data = models.DateField()
    resumo = models.TextField(max_length = 400)
    palavras_chave = models.CharField(max_length = 200)
    universidade = models.CharField(max_length = 200)
    curso = models.CharField(max_length = 200)
    pdf = models.URLField(max_length = 200)

    def __str__(self):
        return self.titulo