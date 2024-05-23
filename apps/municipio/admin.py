from django.contrib import admin
from apps.municipio.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fk_dep', 'date_created', 'date_modified']
