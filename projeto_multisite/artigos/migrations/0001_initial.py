# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('subtitulo', models.CharField(max_length=200, null=True, verbose_name='Subt\xedtulo', blank=True)),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Publica\xe7\xe3o', blank=True)),
                ('texto', models.TextField(max_length=500)),
                ('autor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-data_publicacao',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('data_criacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de cria\xe7\xe3o', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(blank=True, to='artigos.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artigo',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
            preserve_default=True,
        ),
    ]
