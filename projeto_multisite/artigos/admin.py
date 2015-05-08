# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Artigo, Categoria
# from profiles import Profile

class ArtigoAdminSuperForm(forms.ModelForm):
    class Meta:
        model = Artigo
        exclude = []

class ArtigoAdminForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'subtitulo', 'data_publicacao', 'texto', 'categoria', 'autor']

class ArtigoAdmin(admin.ModelForm):
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = ArtigoAdminSuperForm
        else:
            kwargs['form'] = ArtigoAdminForm
        return super(ArtigoAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('titulo', 'data_publicacao', 'categoria', 'autor',)
    list_filter = ['data_publicacao', 'categoria', 'autor', 'site']
    search_fields = ['titulo']
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['autor']

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.save()
        else:
            obj.autor = request.user
            obj.save()

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

# class CategoriaAdmin(admin.ModelForm):
#   pass

# Register your models here.
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Categoria)
