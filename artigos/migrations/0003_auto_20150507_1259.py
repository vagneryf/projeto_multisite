# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('artigos', '0002_artigo_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='content',
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(default=0, blank=True, to='categorias.Categoria'),
            preserve_default=False,
        ),
    ]
