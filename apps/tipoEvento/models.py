from django.db import models

class TipoEvento(models.Model):
    tipo = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.tipo