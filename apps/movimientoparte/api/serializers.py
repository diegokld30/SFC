from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from apps.movimientoparte.models import MovimientoParte
""" REGISTRA """
from apps.movimiento.models import Movimiento
from apps.parteevento.models import ParteEvento
""" listar """
from apps.movimiento.api.serializers import MovimientoSerializer
from apps.parteevento.api.serializers import ParteEventoSerializer


class MovimientoParteSerializer(ModelSerializer):
    fk_parte_evento = PrimaryKeyRelatedField(queryset=ParteEvento.objects.all())
    fk_movimiento = PrimaryKeyRelatedField(queryset=Movimiento.objects.all())

    class Meta:
        model = MovimientoParte
        fields = ['id', 'fk_parte_evento', 'fk_movimiento', 'repeticiones', 'orden', 'date_created']


class Movimiento_listar(ModelSerializer):
    fk_parte_evento = ParteEventoSerializer()
    fk_movimiento = MovimientoSerializer()
    class Meta:
        model = MovimientoParte
        fields = ['id', 'fk_parte_evento', 'fk_movimiento', 'repeticiones', 'orden', 'date_created']