# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Envivo'
        db.create_table(u'envivo_envivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('vivo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'envivo', ['Envivo'])


    def backwards(self, orm):
        # Deleting model 'Envivo'
        db.delete_table(u'envivo_envivo')


    models = {
        u'envivo.envivo': {
            'Meta': {'object_name': 'Envivo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.TextField', [], {}),
            'vivo': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['envivo']