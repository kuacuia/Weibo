# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 10:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='registration_date',
        ),
    ]
