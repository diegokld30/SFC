from rest_framework.viewsets import ModelViewSet
from apps.evento.api.serializers import EventoSerializer
from apps.evento.models import Evento

class EventoViewSet(ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
