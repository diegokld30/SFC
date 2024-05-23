from django.contrib import admin
from apps.rol.models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'date_created', 'date_modified']