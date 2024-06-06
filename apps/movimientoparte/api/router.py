from rest_framework.routers import DefaultRouter

from apps.movimientoparte.api.views import MovimientoParteViewSet

""" listar  los movimientos de la base de datos """
from apps.movimientoparte.api.views import Movimiento_listar_vista
""" listar """
router_movimientoParte = DefaultRouter()
router_movimientoParte.register(prefix="movimientoParte", basename="MovimientoParte", viewset=MovimientoParteViewSet)

""" registrar """
router_movimientoParte.register(prefix="movimientoParteRegist", basename="movimientoParteRegist", viewset=Movimiento_listar_vista)