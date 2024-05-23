from rest_framework import serializers
from apps.movimiento.models import Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ['id', 'nombre', 'slug', 'date_created', 'date_modified']

