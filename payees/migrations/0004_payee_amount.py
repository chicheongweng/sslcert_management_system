# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payees', '0003_payee_payee_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payee',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='amount'),
        ),
    ]
