# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-24 15:25
from __future__ import unicode_literals

from django.db import migrations

from fias.config import TABLES_STATS
from fias.importer.version import fetch_version_info
from fias.importer.commands import load_complete_data


def load_stats_data(apps, schema_editor):
    AddrObj = apps.get_model('fias', 'AddrObj')

    if AddrObj.objects.count():
        fetch_version_info(update_all=True)
        load_complete_data(path=None, truncate=True, tables=TABLES_STATS)


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0004_auto_20160824_1003'),
    ]

    operations = [
        migrations.RunPython(load_stats_data, lambda x, y: x)
    ]
