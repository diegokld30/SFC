"""
URL configuration for SFC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.categoria.api.router import router_categoria
from apps.competicion.api.router import router_competicion
from apps.departamento.api.router import router_dep
from apps.evento.api.router import router_evento
from apps.municipio.api.router import router_mun
from apps.rol.api.router import router_rol
from apps.tipoEvento.api.router import router_tipoEvento
from apps.usuarioEvento.api.router import router_usuarioEvento
from apps.movimiento.api.router import router_movimiento
from apps.parteevento.api.router import router_parteEvento
from apps.movimientoparte.api.router import router_movimientoParte



schema_view = get_schema_view(
   openapi.Info(
      title="Sistema de conteo para competencias de crossfit API V1.0.0",
      default_version='v1',
      description="En esta API se podran contar las reps de cada evento que exista dentro de una competencia especifica",
      terms_of_service="",
      contact=openapi.Contact(email="diegokld23@gmail.com"),
      license=openapi.License(name="Daemon´s Ingenierus"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.user.api.router')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_categoria.urls)),
    path('api/', include(router_competicion.urls)),
    path('api/', include(router_dep.urls)),
    path('api/', include(router_evento.urls)),
    path('api/', include(router_mun.urls)),
    path('api/', include(router_rol.urls)),
    path('api/', include(router_tipoEvento.urls)),
    path('api/', include(router_movimiento.urls)),
    path('api/', include(router_usuarioEvento.urls)),
    path('api/', include(router_parteEvento.urls)),
    path('api/', include(router_movimientoParte.urls)),

]
