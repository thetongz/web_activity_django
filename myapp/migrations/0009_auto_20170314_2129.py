# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20170314_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='days',
            field=models.BigIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')], verbose_name='days:'),
        ),
    ]
