from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.evento.models import Evento
from apps.tipoEvento.models import TipoEvento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fk_categoria', 'fk_tipoEvento', 'cantidadPartes', 'date_start', 'date_end', 'date_modified']
        ref_name = 'CustomEventoSerializer'

    def create(self, validated_data):
        return Evento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fk_categoria = validated_data.get('fk_categoria', instance.fk_categoria)
        instance.fk_tipoEvento = validated_data.get('fk_tipoEvento', instance.fk_tipoEvento)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.cantidadPartes = validated_data.get('cantidadPartes', instance.cantidadPartes)
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.save()
        return instance
