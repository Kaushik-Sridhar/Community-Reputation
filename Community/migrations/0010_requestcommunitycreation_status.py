# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0009_auto_20180102_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcommunitycreation',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
