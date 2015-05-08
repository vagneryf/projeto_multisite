# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.CharField(max_length=200)
	data_criacao = models.DateTimeField(u'Data de criação', default=datetime.now, blank=True)

class Artigo(models.Model):
	titulo = models.CharField(u'Título', max_length=100)
	subtitulo = models.CharField(u'Subtítulo', max_length=200, null=True, blank=True)
	data_publicacao = models.DateTimeField(u'Data de Publicação', default=datetime.now, blank=True)
	texto = models.TextField(max_length=500)
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	autor = models.ForeignKey(User, null=True, blank=True)
	site = models.ForeignKey(Site)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ('-data_publicacao',)
