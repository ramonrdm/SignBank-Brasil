# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0022_auto_20190130_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_used_language',
            field=models.CharField(default='pt-br', max_length=20),
        ),
    ]