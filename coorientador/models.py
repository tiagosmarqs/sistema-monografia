from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Coorientador(models.Model):
    nome = models.CharField(max_length = 200)
    curso = models.CharField(max_length = 200)
    universidade = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100)
    lattes = models.URLField(max_length = 200)
    google_scholar = models.URLField(max_length = 200)
    research_gate = models.URLField(max_length = 200)
    linkedin = models.URLField(max_length = 200)
    orcid = models.URLField(max_length = 200)
    github = models.URLField(max_length = 200)

    def __str__(self):
        return self.nome