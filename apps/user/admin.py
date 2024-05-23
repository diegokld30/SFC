"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)

class UserAdmin(BaseUserAdmin):
    list_display = ['first_name', 'last_name', 'Cedula_persona', 'email','Rol_persona','Telefono_persona','Edad_persona']
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from apps.user.models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'Cedula_persona', 'Edad_persona', 'Telefono_persona', 'Rol_persona', 'fk_municipio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['username', 'last_name', 'Cedula_persona', 'email', 'Rol_persona', 'fk_municipio','Telefono_persona',
                    'Edad_persona']

admin.site.register(User, CustomUserAdmin)