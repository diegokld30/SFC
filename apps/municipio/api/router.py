from rest_framework.routers import DefaultRouter

from apps.municipio.api.views import MunicipioViewSet

router_mun = DefaultRouter()
router_mun.register(prefix='Municipio', basename='Municipio' , viewset=MunicipioViewSet)