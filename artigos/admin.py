from django.contrib import admin
from django import forms
from .models import Artigo
from site_permissions.backends import RestrictSiteMixin
# from tinymce.widgets import TinyMCE

# Register your models here.

class ArtigoAdminForm(forms.ModelForm):
    # texto = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model = Artigo
        exclude = []

class ArtigoAdmin(RestrictSiteMixin, admin.ModelAdmin):
    form = ArtigoAdminForm
    list_display = ('titulo', 'publicacao',)
    list_filter = ['publicacao']
    search_fields = ['titulo', 'texto']

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]
    #         # '/static/tinymce/js/tinymce/tinymce.min.js'

admin.site.register(Artigo, ArtigoAdmin)
