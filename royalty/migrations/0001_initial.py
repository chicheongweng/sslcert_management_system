# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Royalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created At')),
                ('pay_date', models.DateField(verbose_name='Pay Date')),
                ('amount', models.FloatField(verbose_name='Amount')),
            ],
            options={
                'verbose_name': 'Royalty',
                'verbose_name_plural': 'Royalty',
            },
        ),
    ]
