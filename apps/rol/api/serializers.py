from rest_framework import serializers

from apps.rol.models import Rol


class RolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'date_created', 'date_modified']