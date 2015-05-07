# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('informacao', models.TextField(max_length=300, verbose_name='Informa\xe7\xe3o')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
    ]
