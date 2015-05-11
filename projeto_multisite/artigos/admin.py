# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Artigo, Categoria
from django.core.exceptions import ValidationError
# from profiles import Profile

class ArtigoAdminSuperForm(forms.ModelForm):
    class Meta:
        model = Artigo
        exclude = []

class ArtigoAdminForm(forms.ModelForm):
    # def clean(self):
    #     # if not request.user.is_superuser:
    #     #     if obj.site != request.user.site:
    #     #         print 'PASSOU AQUI'
    #     if self.form.categoria == None:
    #         raise ValidationError(u'Você não tem permissão para salvar esse Artigo')
    class Meta:
        model = Artigo
        fields = ['titulo', 'subtitulo', 'data_publicacao', 'texto', 'categoria', 'autor']

class ArtigoAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = ArtigoAdminSuperForm
        else:
            kwargs['form'] = ArtigoAdminForm
        return super(ArtigoAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('titulo', 'data_publicacao', 'categoria', 'get_autor_name', 'site',)
    list_filter = ['site', 'data_publicacao', 'categoria', 'autor']
    search_fields = ['titulo']
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    def get_autor_name(self, obj):
        return obj.autor.get_full_name()
    get_autor_name.short_description = 'Nome do Autor'
    get_autor_name.admin_order_field = 'autor__first_name'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['autor']

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            obj.save()
        else:
            # obj.autor = request.user
            # obj.site = request.user.profile.site
            # obj.save()
            # Testar Try
            # print 'AQUIIIIIII'
            try:
            #     print obj.site
                if obj.site == request.user.profile.site:
                    obj.autor = request.user
                    obj.site = request.user.profile.site
                    obj.save()
            #     else:
            #         print 'NAO TEM PERMISSAO DE SALVAR EM OUTRO SITE'
            #         raise ValidationError('You have not met a constraint!')
            except Exception, e:
            #     # raise
                if request.user.profile:
                    obj.autor = request.user
                    obj.site = request.user.profile.site
                    obj.save()
            #     print 'NAO TEM OBJ, CRIADO NOVO'
            # # else:
            # #     pass
            # # finally:
            # #     pass

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao', 'descricao',)
    search_fields = ['nome']
    readonly_fields = ['data_criacao']

# Register your models here.
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
