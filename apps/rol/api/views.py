from rest_framework.viewsets import ModelViewSet
from apps.rol.models import Rol
from apps.rol.api.serializers import RolSerializer

class RolViewSet(ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()