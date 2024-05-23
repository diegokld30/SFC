from rest_framework import serializers
from apps.tipoEvento.models import TipoEvento

class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ['id', 'tipo', 'date_created', 'date_modified']