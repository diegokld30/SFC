from rest_framework.routers import DefaultRouter

from apps.competicion.api.views import CompeticionViewSet

router_competicion = DefaultRouter()
router_competicion.register(prefix='competicion', basename='competicion', viewset=CompeticionViewSet)