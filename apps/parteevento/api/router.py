from rest_framework.routers import DefaultRouter

from apps.parteevento.api.views import ParteEventoViewSet

router_parteEvento = DefaultRouter()
router_parteEvento.register(prefix="parteEvento", basename="parteEvento", viewset=ParteEventoViewSet)