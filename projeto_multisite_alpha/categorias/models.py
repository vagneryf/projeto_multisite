# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    informacao = models.TextField(u'Informação', max_length=300)
    site = models.ForeignKey(Site)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)