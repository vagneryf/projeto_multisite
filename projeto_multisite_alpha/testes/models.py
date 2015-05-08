# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Secao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(u'Descrição', max_length=200)
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ('id',)

class Teste(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    publicacao = models.DateTimeField(u'Data de Publicação', default=datetime.now, blank=True)
    texto = models.TextField(max_length=300)
    publicado_por = models.ForeignKey(User, null=True, blank=True) #, editable=False)
    secao = models.ForeignKey(Secao, null=True, blank=True) #, default=lambda: Secao.objects.get(id=1))

    def __unicode__(self):
        return u'Teste - %s' % self.titulo

    class Meta:
        ordering = ('-publicacao',)