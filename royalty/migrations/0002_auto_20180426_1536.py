# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royalty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='royalty',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]
