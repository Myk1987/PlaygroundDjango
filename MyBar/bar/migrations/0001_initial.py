# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('glass', models.CharField(max_length=100)),
                ('recipe', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=400)),
                ('history', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.CharField(max_length=100)),
                ('coctail', models.ForeignKey(to='bar.Cocktail')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('alcohol', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='components',
            name='ingredient',
            field=models.ForeignKey(to='bar.Ingredient'),
        ),
    ]
