# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Teste, Secao
from django import forms 
import re

# Register your models here.

# class SecaoAdmin(admin.ModelAdmin):
#     pass

# class FiltrarSecao(admin.SimpleListFilter):
#     title = u'Filtro Seção'
#     parameter_name = 'sec'

#     def lookups(self, request, model_admin):
#         return (
#             ('1', ('Secao 1')),
#             ('2', ('Secao 2')),
#         )

#     def queryset(self, request, queryset):
#         if self.value() == '1':
#             return queryset.filter(secao=1)
#         if self.value() == '2':
#             return queryset.filter(secao=2)

class TesteAdminForm(forms.ModelForm):
    # secao = forms.CharField()
    class Meta:
        model = Teste
        exclude =[]

    def __init__(self, *args, **kwargs):
        super(TesteAdminForm, self).__init__(*args, **kwargs)
        secao = Secao.objects.filter(id=1)
        print 'AQUI!!!!!'
        # print self.instance.request.user
        # if self.instance.request.user == 2:
        #     secao = Secao.objects.filter(id=2)
        # self.fields['secao'].widget.attrs['readonly'] = True
        # self.fields['secao'].default = lambda: Secao.objects.get(id=1)
        self.fields['secao'].queryset = secao

    def clean_publicado_por(self):
        # print self.cleaned_datapublicado_por
        return self.cleaned_data["publicado_por"]



class TesteAdmin(admin.ModelAdmin):
    form = TesteAdminForm
    list_display = ('titulo', 'publicacao', 'secao',)
    list_filter = ['publicacao', 'secao']
    search_fields = ['titulo']
    # exclude = ['publicado_por']
    # para mostrar os filtros como o admin default do Django:
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    # def get_form(self, req, obj=None, **kwargs):
    #     # save the currently logged in user for later
    #     self.current_user = req.user
    #     return super(TesteAdmin, self).get_form(req, obj, **kwargs)

    # def formfield_for_dbfield(self, field, **kwargs):
    #     from django import forms
    #     from django.contrib.auth import models
    #     if field.name == 'publicado_por':
    #         queryset = models.User.objects.all()
    #         return forms.ModelChoiceField(
    #             queryset=queryset, initial=self.current_userself.id)
    #     return super(TesteAdmin, self).formfield_for_dbfield(field, **kwargs)

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

admin.site.register(Teste, TesteAdmin)
admin.site.register(Secao) # , SecaoAdmin)