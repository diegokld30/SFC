from django.contrib import admin
from apps.parteevento.models import ParteEvento

@admin.register(ParteEvento)
class ParteEventoAdmin(admin.ModelAdmin):
    list_display = ['fk_evento', 'orden', 'timecap', 'descanso', 'date_created']