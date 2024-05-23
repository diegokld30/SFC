from rest_framework.routers import DefaultRouter
from apps.usuarioEvento.api.views import EventoViewSet

router_usuarioEvento = DefaultRouter()
router_usuarioEvento.register(prefix='usuarioEvento', basename='usuarioEvento', viewset=EventoViewSet)