from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import SET_NULL
from apps.rol.models import Rol
from apps.municipio.models import Municipio
from apps.evento.models import Evento

class User(AbstractUser):
    Cedula_persona = models.CharField(max_length=255, blank=True)
    Edad_persona = models.CharField(max_length=100)
    Telefono_persona = models.CharField(max_length=255)
    Rol_persona = models.ForeignKey(Rol, on_delete=SET_NULL, null=True, blank=True)
    fk_municipio = models.ForeignKey(Municipio, on_delete=SET_NULL, null=True, blank=True)
    #fk_evento = models.ForeignKey(Evento, on_delete=SET_NULL, null=True, blank=True)

    # Con esto se configura que se debe iniciar sesion con el email
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []