# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teste',
            name='secao',
            field=models.ForeignKey(blank=True, to='testes.Secao', null=True),
            preserve_default=True,
        ),
    ]
