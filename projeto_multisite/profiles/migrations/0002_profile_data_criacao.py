# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de cria\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
    ]
