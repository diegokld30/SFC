from rest_framework.viewsets import ModelViewSet
from apps.categoria.api.serializers import CategoriaSerializer
from apps.categoria.models import Categoria

class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()