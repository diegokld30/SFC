from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from apps.parteevento.models import ParteEvento
from apps.evento.models import Evento

class ParteEventoSerializer(serializers.ModelSerializer):
    fk_evento = PrimaryKeyRelatedField(queryset=Evento.objects.all())

    class Meta:
        model = ParteEvento
        fields = ['id', 'fk_evento', 'orden', 'timecap', 'descanso', 'date_created']

    def create(self, validated_data):
        fk_evento = validated_data.pop('fk_evento')
        parte_evento = ParteEvento.objects.create(fk_evento=fk_evento, **validated_data)
        return parte_evento
