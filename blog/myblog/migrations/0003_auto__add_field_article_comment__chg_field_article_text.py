# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.comment'
        db.add_column(u'myblog_article', 'comment',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=200),
                      keep_default=False)


        # Changing field 'Article.text'
        db.alter_column(u'myblog_article', 'text', self.gf('django.db.models.fields.TextField')(max_length=1000000000))

    def backwards(self, orm):
        # Deleting field 'Article.comment'
        db.delete_column(u'myblog_article', 'comment')


        # Changing field 'Article.text'
        db.alter_column(u'myblog_article', 'text', self.gf('django.db.models.fields.CharField')(max_length=1000000000000))

    models = {
        u'myblog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myblog.Author']"}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1000000000'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'myblog.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['myblog']