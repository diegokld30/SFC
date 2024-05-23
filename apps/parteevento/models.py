from django.db import models
from django.db.models import SET_NULL
from apps.evento.models import Evento

class ParteEvento(models.Model):
    fk_evento = models.ForeignKey(Evento, on_delete=SET_NULL, null=True)
    orden = models.IntegerField()
    timecap = models.CharField(max_length=100, null=True)
    descanso = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fk_evento)