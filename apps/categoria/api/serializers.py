from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.competicion.models import Competicion
from apps.competicion.api.serializers import CompeticionSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    fk_competencia = CompeticionSerializer()
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'fk_competencia', 'date_created', 'date_modified']