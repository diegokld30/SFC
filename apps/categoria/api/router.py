from rest_framework.routers import DefaultRouter

from apps.categoria.api.views import CategoriaViewSet

router_categoria = DefaultRouter()
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaViewSet)