from django.contrib import admin
from apps.categoria.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fk_competencia', 'date_created', 'date_modified']