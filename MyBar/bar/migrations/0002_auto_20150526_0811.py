# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='components',
            old_name='coctail',
            new_name='cocktail',
        ),
    ]
