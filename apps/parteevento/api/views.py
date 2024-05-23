from rest_framework.viewsets import ModelViewSet
from apps.parteevento.api.serializers import ParteEventoSerializer
from apps.parteevento.models import ParteEvento


class ParteEventoViewSet(ModelViewSet):
    serializer_class = ParteEventoSerializer
    queryset = ParteEvento.objects.all()