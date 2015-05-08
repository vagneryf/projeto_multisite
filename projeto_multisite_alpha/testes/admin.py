# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Teste, Secao
from django import forms 
import re

# Register your models here.

# class SecaoAdmin(admin.ModelAdmin):
#     pass

class TesteAdminForm(forms.ModelForm):
    # secao = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super(TesteAdminForm, self).__init__(*args, **kwargs)
    #     secao = Secao.objects.filter(id=1)
    #     print 'AQUI!!!!!'
    #     # print self.instance.request.user
    #     # if self.instance.request.user == 2:
    #     #     secao = Secao.objects.filter(id=2)
    #     # self.fields['secao'].widget.attrs['readonly'] = True
    #     # self.fields['secao'].default = lambda: Secao.objects.get(id=1)
    #     self.fields['secao'].queryset = secao

    # readonly_fields = ('publicado_por',)

    class Meta:
        fields = ['titulo', 'publicacao', 'texto', 'publicado_por']
        model = Teste
        # exclude = ['secao']

    # def clean_publicado_por(self):
    #     # print self.cleaned_datapublicado_por
    #     return self.cleaned_data["publicado_por"]

class TesteAdminSuperForm(forms.ModelForm):
    class Meta:
        fields = ['titulo', 'publicacao', 'texto', 'secao', 'publicado_por']
        model= Teste

class TesteAdmin(admin.ModelAdmin):
    # form = TesteAdminForm
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = TesteAdminSuperForm
        else:
            kwargs['form'] = TesteAdminForm
        return super(TesteAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('titulo', 'publicacao', 'secao', 'publicado_por',)
    list_filter = ['publicacao', 'secao', 'publicado_por']
    search_fields = ['titulo']
    # para mostrar os filtros como o admin default do Django:
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['publicado_por']
    # exclude = ['secao']
    # readonly_fields = ['publicado_por']
    
    # def get_form(self, request, obj=None, **kwargs):
    #     # save the currently logged in user for later
    #     self.current_user = request.user
    #     return super(TesteAdmin, self).get_form(request, obj, **kwargs)

    # def formfield_for_dbfield(self, field, **kwargs):
    #     from django import forms
    #     from django.contrib.auth import models
    #     if field.name == 'publicado_por':
    #         queryset = models.User.objects.all()
    #         return forms.ModelChoiceField(
    #             queryset=queryset, initial=self.current_userself.id)
    #     return super(TesteAdmin, self).formfield_for_dbfield(field, **kwargs)


    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.save()
        else:
            obj.publicado_por = request.user
            obj.save()

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

admin.site.register(Teste, TesteAdmin)
admin.site.register(Secao) # , SecaoAdmin)