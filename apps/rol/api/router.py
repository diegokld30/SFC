from rest_framework.routers import DefaultRouter
from apps.rol.api.views import RolViewSet

router_rol = DefaultRouter()
router_rol.register(prefix='Rol', basename='Rol', viewset=RolViewSet)

