# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0009_group_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(null=True, upload_to='group'),
        ),
    ]