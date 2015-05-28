# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('public', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='box_created_by', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'boxes',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('front', models.TextField()),
                ('back', models.TextField(null=True, blank=True)),
                ('enable', models.BooleanField(default=True)),
                ('label', models.CharField(max_length=512, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='card_created_by', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('short', models.CharField(max_length=512, null=True, blank=True)),
                ('title', models.CharField(max_length=512)),
                ('enable', models.BooleanField(default=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='karte.Box', null=True)),
                ('created_by', models.ForeignKey(related_name='sec_created_by', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('short', models.CharField(max_length=512, null=True, blank=True)),
                ('title', models.CharField(max_length=512, blank=True)),
                ('enable', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='sub_created_by', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='karte.Section', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='subsection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='karte.Subsection', null=True),
        ),
    ]
