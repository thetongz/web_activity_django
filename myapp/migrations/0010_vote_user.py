# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-14 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20170314_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]