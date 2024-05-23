from rest_framework.viewsets import ModelViewSet
from apps.movimientoparte.api.serializers import MovimientoParteSerializer
from apps.movimientoparte.models import MovimientoParte


class MovimientoParteViewSet(ModelViewSet):
    serializer_class = MovimientoParteSerializer
    queryset = MovimientoParte.objects.all()