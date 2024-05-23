from rest_framework.viewsets import ModelViewSet
from apps.tipoEvento.api.serializers import TipoEventoSerializer
from apps.tipoEvento.models import TipoEvento

class TipoEventoViewSet(ModelViewSet):
    serializer_class = TipoEventoSerializer
    queryset = TipoEvento.objects.all()