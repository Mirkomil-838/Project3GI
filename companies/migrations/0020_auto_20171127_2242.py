# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0019_mineownership_in_use'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineownership',
            name='in_use',
        ),
        migrations.AddField(
            model_name='ownership',
            name='in_use',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
