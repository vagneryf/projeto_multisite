from django.contrib import admin
from .models import Artigo

# Register your models here.

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao',)
    list_filter = ['publicacao']
    search_fields = ['titulo', 'texto']

admin.site.register(Artigo, ArtigoAdmin)
