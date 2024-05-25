from django.contrib import admin
from apps.competicion.models import Competicion

@admin.register(Competicion)
class CompeticionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'state', 'date_created', 'date_finished', 'date_updated']

