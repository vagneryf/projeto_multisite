# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    publicacao = models.DateTimeField(u'Data de Publicação', default=datetime.now, blank=True)
    texto = models.TextField(max_length=300)

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ('-id',)
