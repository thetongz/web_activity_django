# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170314_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allergies', models.BigIntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Allergies:')),
            ],
        ),
    ]