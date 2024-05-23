from django.contrib import admin

from apps.movimientoparte.models import MovimientoParte


@admin.register(MovimientoParte)
class MovimientoParteAdmin(admin.ModelAdmin):
    list_display = ['fk_parte_evento', 'fk_movimiento', 'repeticiones', 'orden','date_created' ]