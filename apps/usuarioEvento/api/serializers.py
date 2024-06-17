from rest_framework import serializers
from apps.usuarioEvento.models import usuarioEvento
from apps.user.models import User
from apps.evento.models import Evento
from rest_framework.serializers import PrimaryKeyRelatedField

class UsuarioEventoSerializer(serializers.ModelSerializer):
    fk_user = PrimaryKeyRelatedField(queryset=User.objects.all())
    fk_evento = PrimaryKeyRelatedField(queryset=Evento.objects.all())


    class Meta:
        model = usuarioEvento
        fields = ['id','fk_user','fk_evento','conteo_reps','date_start','date_end','date_modified']

    def create(self, validated_data):
        fk_user = validated_data.pop('fk_user')
        fk_evento = validated_data.pop('fk_evento')

        usuario_evento = usuarioEvento.objects.create(fk_user=fk_user, fk_evento=fk_evento, **validated_data)
        return usuario_evento