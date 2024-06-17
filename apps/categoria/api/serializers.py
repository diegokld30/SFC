from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from apps.categoria.models import Categoria
from apps.competicion.models import Competicion


class CategoriaSerializer(serializers.ModelSerializer):
    fk_competencia = PrimaryKeyRelatedField(queryset=Competicion.objects.all())

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'fk_competencia', 'date_created', 'date_modified']

    def create(self, validated_data):
        competencia = validated_data.pop('fk_competencia')
        categoria = Categoria.objects.create(fk_competencia=competencia, **validated_data)
        return categoria

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        competencia = validated_data.get('fk_competencia', None)
        if competencia:
            instance.fk_competencia = competencia
        instance.save()
        return instance
