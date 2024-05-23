from rest_framework.routers import DefaultRouter

from apps.departamento.api.views import DepartamentoViewSet

router_dep = DefaultRouter()
router_dep.register(prefix='Departamento', basename='Departamento', viewset=DepartamentoViewSet)