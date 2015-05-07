from django.contrib import admin
from .models import Categoria
from site_permissions.backends import RestrictSiteMixin

# Register your models here.

class CategoriaAdmin(RestrictSiteMixin, admin.ModelAdmin):
    list_display = ('nome', 'id', 'data_criacao',)

admin.site.register(Categoria, CategoriaAdmin)
