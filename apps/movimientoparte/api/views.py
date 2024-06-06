from rest_framework.viewsets import ModelViewSet
from apps.movimientoparte.api.serializers import MovimientoParteSerializer
from apps.movimientoparte.models import MovimientoParte

""" listar """
from apps.movimientoparte.api.serializers import Movimiento_listar
""" listar """
class MovimientoParteViewSet(ModelViewSet):
    serializer_class = MovimientoParteSerializer
    queryset = MovimientoParte.objects.all()
    http_method_names= ['post', 'put',]

""" Registrar """
class Movimiento_listar_vista(ModelViewSet):
    serializer_class = Movimiento_listar
    queryset = MovimientoParte.objects.all()
    http_method_names= ['get', 'delete']