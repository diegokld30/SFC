from rest_framework.routers import DefaultRouter

from apps.movimientoparte.api.views import MovimientoParteViewSet

router_movimientoParte = DefaultRouter()
router_movimientoParte.register(prefix="movimientoParte", basename="MovimientoParte", viewset=MovimientoParteViewSet)
