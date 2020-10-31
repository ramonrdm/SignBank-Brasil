# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-29 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0036_auto_20200930_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localization',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='localization',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.Localization', verbose_name='Localização Pai'),
        ),
    ]