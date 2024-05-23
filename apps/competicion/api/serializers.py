from rest_framework import serializers
from apps.competicion.models import Competicion


class CompeticionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicion
        fields = ['id', 'nombre', 'state', 'date_created', 'date_finished', 'date_finished']

