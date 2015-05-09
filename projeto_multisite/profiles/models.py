# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    site = models.ForeignKey(Site)
    data_criacao = models.DateTimeField(u'Data de criação', default=datetime.now, blank=True)

    def __unicode__(self):
        return u'Profile: %s' % self.user

    class Meta:
        ordering = ('user',)