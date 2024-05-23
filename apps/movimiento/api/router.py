from rest_framework.routers import DefaultRouter
from apps.movimiento.api.views import MovimientoViewSet

router_movimiento = DefaultRouter()
router_movimiento.register(prefix="movimiento", basename="movimiento", viewset=MovimientoViewSet)