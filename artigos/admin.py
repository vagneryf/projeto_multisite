from django.contrib import admin
from .models import Artigo
from site_permissions.backends import RestrictSiteMixin

# Register your models here.

class ArtigoAdmin(RestrictSiteMixin, admin.ModelAdmin):
    list_display = ('titulo', 'publicacao',)
    list_filter = ['publicacao']
    search_fields = ['titulo', 'texto']

admin.site.register(Artigo, ArtigoAdmin)
