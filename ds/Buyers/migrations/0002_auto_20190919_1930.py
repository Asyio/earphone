# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-19 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='isactive',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='portrait',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='signature',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
