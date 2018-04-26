# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payee',
            name='amount',
        ),
        migrations.AddField(
            model_name='payee',
            name='percentage',
            field=models.FloatField(default=0.0, verbose_name='percentage'),
        ),
    ]
