from django.contrib import admin
from apps.departamento.models import Departamento

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'date_created', 'date_modified']


