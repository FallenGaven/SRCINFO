# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 12:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRCCompany', '0010_auto_20171210_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plug',
            old_name='plug_subdomain',
            new_name='plug_webinfo',
        ),
    ]
