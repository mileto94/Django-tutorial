# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'myblog_comment')


        # Renaming column for 'Article.comment' to match new field type.
        db.rename_column(u'myblog_article', 'comment_id', 'comment')
        # Changing field 'Article.comment'
        db.alter_column(u'myblog_article', 'comment', self.gf('django.db.models.fields.TextField')(max_length=300))
        # Removing index on 'Article', fields ['comment']
        db.delete_index(u'myblog_article', ['comment_id'])


    def backwards(self, orm):
        # Adding index on 'Article', fields ['comment']
        db.create_index(u'myblog_article', ['comment_id'])

        # Adding model 'Comment'
        db.create_table(u'myblog_comment', (
            ('comment_body', self.gf('django.db.models.fields.TextField')(default='', max_length=300)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'myblog', ['Comment'])


        # Renaming column for 'Article.comment' to match new field type.
        db.rename_column(u'myblog_article', 'comment', 'comment_id')
        # Changing field 'Article.comment'
        db.alter_column(u'myblog_article', 'comment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myblog.Comment']))

    models = {
        u'myblog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myblog.Author']"}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '300'}),
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
        }
    }

    complete_apps = ['myblog']