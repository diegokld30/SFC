from rest_framework import serializers
from apps.parteevento.models import ParteEvento
from apps.evento.api.serializers import EventoSerializer

class ParteEventoSerializer(serializers.ModelSerializer):
    fk_evento = EventoSerializer()

    class Meta:
        model = ParteEvento
        fields = ['id', 'fk_evento', 'orden', 'timecap', 'descanso', 'date_created']