from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.competicion.models import Competicion
from apps.competicion.api.serializers import CompeticionSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    fk_competencia = CompeticionSerializer()
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'fk_competencia', 'date_created', 'date_modified']

    def create(self, validated_data):
        competencia_data = validated_data.pop('fk_competencia')
        competencia, created = Competicion.objects.get_or_create(**competencia_data)
        categoria = Categoria.objects.create(fk_competencia=competencia, **validated_data)
        return categoria