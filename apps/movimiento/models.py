from django.db import models
from django.db.models import SET_NULL

class Movimiento(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
