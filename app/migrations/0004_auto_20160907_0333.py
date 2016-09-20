# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160828_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibo',
            name='forward_or_collect_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forward_or_collects', to='app.Weibo'),
        ),
        migrations.AddField(
            model_name='weibo',
            name='wb_type',
            field=models.IntegerField(choices=[(0, 'new'), (1, 'forward'), (2, 'collect')], default=0),
        ),
    ]
