# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_auto_20150526_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='link_name',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
