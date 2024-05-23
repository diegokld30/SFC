from rest_framework.viewsets import ModelViewSet
from apps.departamento.api.serializers import DepartamentoSerializer
from apps.departamento.models import Departamento


class DepartamentoViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()