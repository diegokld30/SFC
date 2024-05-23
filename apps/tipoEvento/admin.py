from django.contrib import admin
from apps.tipoEvento.models import TipoEvento


@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'date_created', 'date_modified']