from rest_framework.viewsets import ModelViewSet
from apps.movimiento.api.serializers import MovimientoSerializer
from apps.movimiento.models import Movimiento

class MovimientoViewSet(ModelViewSet):
    serializer_class = MovimientoSerializer
    queryset = Movimiento.objects.all()