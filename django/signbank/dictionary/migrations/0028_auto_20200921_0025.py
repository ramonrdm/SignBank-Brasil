# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-20 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0027_auto_20200303_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gloss',
            name='absOriFing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Absolute Orientation: Fingers'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='absOriPalm',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Absolute Orientation: Palm'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='contType',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Contact Type'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='derivHist',
            field=models.CharField(blank=True, max_length=50, verbose_name='Derivation history'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='domFlex',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Dominant hand - Flexion'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='domSF',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Dominant hand - Selected Fingers'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='final_loc',
            field=models.IntegerField(blank=True, null=True, verbose_name='Final Primary Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='final_secondary_loc',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Final Subordinate Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='handCh',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Handshape Change'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='handedness',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Handedness'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='iconType',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Type of iconicity'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='initial_secondary_loc',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Initial Subordinate Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locPrimLH',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Placement Active Articulator LH'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locprim',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locsecond',
            field=models.IntegerField(blank=True, null=True, verbose_name='Secondary Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='movDir',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Movement Direction'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='movMan',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Movement Manner'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='movSh',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Movement Shape'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='namEnt',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Named Entity'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='oriCh',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Orientation Change'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='relOriLoc',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Relative Orientation: Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='relOriMov',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Relative Orientation: Movement'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='relatArtic',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Relation between Articulators'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='semField',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Semantic Field'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='valence',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Valence'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='wordClass',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Word class'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='wordClass2',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Word class 2'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsAperture',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Aperture'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsFingConf',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Finger configuration'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsFingConf2',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Finger configuration 2'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsFingSel',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Finger selection'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsFingSel2',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Finger selection 2'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsFingUnsel',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Unselected fingers'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsNumSel',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsSpread',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Spreading'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='hsThumb',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Thumb'),
        ),
        migrations.AlterField(
            model_name='morpheme',
            name='mrpType',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='morphologydefinition',
            name='role',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='othermedia',
            name='type',
            field=models.CharField(max_length=5),
        ),
    ]
