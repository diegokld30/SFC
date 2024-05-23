from rest_framework.serializers import ModelSerializer

from apps.movimientoparte.models import MovimientoParte

from apps.movimiento.api.serializers import MovimientoSerializer
from apps.parteevento.api.serializers import ParteEventoSerializer


class MovimientoParteSerializer(ModelSerializer):
    fk_parte_evento = ParteEventoSerializer()
    fk_movimiento = MovimientoSerializer()

    class Meta:
        model = MovimientoParte
        fields = ['id', 'fk_parte_evento', 'fk_movimiento', 'repeticiones', 'orden','date_created' ]