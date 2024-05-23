from rest_framework.viewsets import ModelViewSet
from apps.municipio.api.serializers import MunicipioSerializer
from apps.municipio.models import Municipio

class MunicipioViewSet(ModelViewSet):
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()