# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Comment.comment'
        db.delete_column(u'myblog_comment', 'comment')

        # Adding field 'Comment.comment_body'
        db.add_column(u'myblog_comment', 'comment_body',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Comment.comment'
        db.add_column(u'myblog_comment', 'comment',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300),
                      keep_default=False)

        # Deleting field 'Comment.comment_body'
        db.delete_column(u'myblog_comment', 'comment_body')


    models = {
        u'myblog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myblog.Author']"}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myblog.Comment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'http://cdn.theanimals.pics/pictures/www.thedesignwork.com/wp-content/uploads/2011/03/lightning-huntington-beach-national-geographic-wallpaper.jpg'", 'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '1000000000'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'myblog.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'myblog.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_body': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['myblog']