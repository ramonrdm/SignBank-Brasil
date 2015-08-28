# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


from tagging.models import Tag


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."

        for gloss in orm.Gloss.objects.all():
            if gloss.InMedLex:
                 Tag.objects.add_tag(gloss, 'workflow:problematic')

    def backwards(self, orm):
        "Write your backwards methods here."

        for gloss in orm.Gloss.objects.all():
            Tag.objects.get_for_object(gloss).filter(name='workflow:problematic').delete()



    models = {
        'dictionary.definition': {
            'Meta': {'ordering': "['gloss']", 'object_name': 'Definition'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'gloss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Gloss']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'dictionary.dialect': {
            'Meta': {'ordering': "['language', 'name']", 'object_name': 'Dialect'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'dictionary.gloss': {
            'BookProb': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'InMainBook': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'InMedLex': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'InSuppBook': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['idgloss']", 'object_name': 'Gloss'},
            'NotBkDBOnly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Palm_orientation': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'SpecialCore': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'StemSN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'annotation_idgloss': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'aslgloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'asloantf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'asltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'blend': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'blendtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bslgloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'bslloantf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bsltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comp': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'compound': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comptf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dialect': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dictionary.Dialect']", 'symmetrical': 'False'}),
            'domhndsh': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idgloss': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'inCD': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'inWeb': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'inittext': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'blank': 'True'}),
            'inittf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'isNew': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dictionary.Language']", 'symmetrical': 'False'}),
            'locprim': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'locsecond': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'morph': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'queries': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sedefinetf': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'segloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sense': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'subhndsh': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'tjspeculate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'dictionary.keyword': {
            'Meta': {'ordering': "['text']", 'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'dictionary.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'dictionary.relation': {
            'Meta': {'ordering': "['source']", 'object_name': 'Relation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relation_sources'", 'to': "orm['dictionary.Gloss']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relation_targets'", 'to': "orm['dictionary.Gloss']"})
        },
        'dictionary.translation': {
            'Meta': {'ordering': "['gloss', 'index']", 'object_name': 'Translation'},
            'gloss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Gloss']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Keyword']"})
        }
    }

    complete_apps = ['dictionary']
    symmetrical = True
