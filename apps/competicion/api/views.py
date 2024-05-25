from rest_framework.viewsets import ModelViewSet
from apps.competicion.api.serializers import CompeticionSerializer
from apps.competicion.models import Competicion
from apps.competicion.api.permissions import IsOwnerOrReadOnly

class CompeticionViewSet(ModelViewSet):
    #permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CompeticionSerializer
    queryset = Competicion.objects.all()