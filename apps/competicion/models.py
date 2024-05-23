from django.db import models

class Competicion(models.Model):
    nombre = models.CharField(max_length=100)
    state = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    date_finished = models.DateTimeField(auto_now=True)
    date_updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre