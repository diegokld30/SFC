from django.db import models
from django.db.models import SET_NULL
from apps.movimiento.models import Movimiento
from apps.parteevento.models import ParteEvento

class MovimientoParte(models.Model):
    fk_parte_evento = models.ForeignKey(ParteEvento, on_delete=SET_NULL, null=True)
    fk_movimiento = models.ForeignKey(Movimiento, on_delete=SET_NULL, null=True)
    repeticiones = models.CharField(max_length=100)  # Cadena que representa la secuencia de repeticiones, debe recibir un texto o arreglo
    orden = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fk_parte_evento)
