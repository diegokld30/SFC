from rest_framework.viewsets import ModelViewSet
from apps.usuarioEvento.api.serializers import UsuarioEventoSerializer
from apps.usuarioEvento.models import usuarioEvento
from apps.usuarioEvento.api.permissions import IsOwnerOrReadOnly

class EventoViewSet(ModelViewSet):
    #permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UsuarioEventoSerializer
    queryset = usuarioEvento.objects.all()