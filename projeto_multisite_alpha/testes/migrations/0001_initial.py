# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Publica\xe7\xe3o', blank=True)),
                ('texto', models.TextField(max_length=300)),
            ],
            options={
                'ordering': ('-publicacao',),
            },
            bases=(models.Model,),
        ),
    ]
