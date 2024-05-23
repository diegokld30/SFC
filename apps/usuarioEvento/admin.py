from django.contrib import admin
from apps.usuarioEvento.models import usuarioEvento

@admin.register(usuarioEvento)
class usuarioEventoAdmin(admin.ModelAdmin):
    list_display = ['fk_user','fk_evento','conteo_reps','date_start','date_end','date_modified']