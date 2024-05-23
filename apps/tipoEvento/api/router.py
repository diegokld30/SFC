from rest_framework.routers import DefaultRouter

from apps.tipoEvento.api.views import TipoEventoViewSet

router_tipoEvento = DefaultRouter()
router_tipoEvento.register(prefix='tipoevento', basename='tipoevento', viewset=TipoEventoViewSet)