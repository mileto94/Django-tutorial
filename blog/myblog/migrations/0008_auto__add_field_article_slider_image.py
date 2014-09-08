# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.slider_image'
        db.add_column(u'myblog_article', 'slider_image',
                      self.gf('django.db.models.fields.URLField')(default='static/light.jpg', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.slider_image'
        db.delete_column(u'myblog_article', 'slider_image')


    models = {
        u'myblog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myblog.Author']"}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'static/light.jpg'", 'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slider_image': ('django.db.models.fields.URLField', [], {'default': "'static/light.jpg'", 'max_length': '200'}),
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