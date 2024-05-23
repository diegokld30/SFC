from django.db import models
from django.db.models import SET_NULL
from apps.user.models import User
from apps.evento.models import Evento

class usuarioEvento(models.Model):
    fk_user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    fk_evento = models.ForeignKey(Evento, on_delete=SET_NULL, null=True)
    conteo_reps = models.CharField(max_length=100, null=True, blank=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    date_modified = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.fk_user)


