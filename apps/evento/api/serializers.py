from rest_framework import serializers
from apps.categoria.api.serializers import CategoriaSerializer
from apps.evento.models import Evento
from apps.tipoEvento.api.serializers import TipoEventoSerializer


class EventoSerializer(serializers.ModelSerializer):
    fk_categoria = CategoriaSerializer()
    fk_tipoEvento = TipoEventoSerializer()

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fk_categoria', 'fk_tipoEvento','cantidadPartes', 'date_start','date_end', 'date_modified']
        ref_name = 'CustomEventoSerializer'
