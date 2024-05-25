from rest_framework import serializers
from apps.user.models import User
from apps.rol.models import Rol
from apps.rol.api.serializers import RolSerializer
from apps.municipio.models import Municipio


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'Cedula_persona', 'Edad_persona', 'Telefono_persona',
                  'Rol_persona', 'fk_municipio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        rol_data = validated_data.pop('Rol_persona', None)
        municipio_data = validated_data.pop('fk_municipio', None)

        if rol_data:
            rol = Rol.objects.get_or_create(**rol_data)[0]
            validated_data['Rol_persona'] = rol

        if municipio_data:
            municipio = Municipio.objects.get_or_create(**municipio_data)[0]
            validated_data['fk_municipio'] = municipio

        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


# Clase para mostrar los datos del usuario
class UserSerializer(serializers.ModelSerializer):
    Rol_persona = RolSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'Cedula_persona', 'Edad_persona', 'Telefono_persona', 'Rol_persona',
                  'fk_municipio', 'first_name', 'last_name']


# Clase para actualizar los datos del usuario
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'Rol_persona', 'Cedula_persona', 'Edad_persona', 'Telefono_persona',
                  'fk_municipio']
