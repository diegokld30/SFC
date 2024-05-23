from rest_framework import serializers
from apps.usuarioEvento.models import usuarioEvento
from apps.user.models import User
from apps.evento.models import Evento
from apps.user.api.serializers import UserSerializer
from apps.evento.api.serializers import EventoSerializer

class UsuarioEventoSerializer(serializers.ModelSerializer):
    fk_user = UserSerializer()
    fk_evento = EventoSerializer()
    #fk_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #fk_evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())

    class Meta:
        model = usuarioEvento
        fields = ['id','fk_user','fk_evento','conteo_reps','date_start','date_end','date_modified']