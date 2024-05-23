from django.contrib import admin

from apps.movimiento.models import Movimiento


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'date_created', 'date_modified']

