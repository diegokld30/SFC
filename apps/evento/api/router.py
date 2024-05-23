from rest_framework.routers import DefaultRouter

from apps.evento.api.views import EventoViewSet

router_evento = DefaultRouter()
router_evento.register(prefix='evento', basename='Evento', viewset=EventoViewSet)