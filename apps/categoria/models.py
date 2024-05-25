from django.db import models
from django.db.models import SET_NULL
from apps.competicion.models import Competicion

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fk_competencia = models.ForeignKey(Competicion, on_delete=SET_NULL, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

