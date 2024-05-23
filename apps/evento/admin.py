from django.contrib import admin
from apps.evento.models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = [ 'nombre', 'fk_categoria', 'fk_tipoEvento','cantidadPartes', 'date_start','date_end', 'date_modified']