from django.db import models
from django.db.models import SET_NULL
from apps.departamento.models import Departamento


class Municipio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    fk_dep = models.ForeignKey(Departamento, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre