from django.db import models
from django.db.models import SET_NULL
from apps.categoria.models import Categoria
from apps.tipoEvento.models import TipoEvento
from apps.movimiento.models import Movimiento


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fk_categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True)
    fk_tipoEvento = models.ForeignKey(TipoEvento, on_delete=SET_NULL, null=True)
    #fk_movimiento = models.ForeignKey(Movimiento, on_delete=SET_NULL, null=True)
    cantidadPartes = models.IntegerField(default=1)
    #descanso = models.IntegerField(default=0)
    #timecap = models.CharField(max_length=100, null=True)
    date_start = models.DateField()
    date_end = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre