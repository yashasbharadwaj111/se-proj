# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0006_auto_20191122_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmark',
            name='comments',
            field=models.CharField(default='', max_length=3000),
        ),
    ]