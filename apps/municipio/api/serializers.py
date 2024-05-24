from rest_framework import serializers
from apps.municipio.models import Municipio
from apps.departamento.api.serializers import DepartamentoSerializer


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        fk_dep = DepartamentoSerializer()
        model = Municipio
        fields = ['id', 'nombre', 'fk_dep', 'date_created', 'date_modified']

    def validate_municipio(self, value):
        if Municipio.objects.filter(nombre=value).exists():
            raise serializers.ValidationError("El municipio ya existe")
        return value