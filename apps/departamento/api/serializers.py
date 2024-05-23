from rest_framework import serializers
from apps.departamento.models import Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nombre', 'date_created', 'date_modified']