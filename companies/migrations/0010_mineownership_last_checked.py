# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 00:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_company_locationz'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineownership',
            name='last_checked',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 0, 23, 16, 824000, tzinfo=utc)),
        ),
    ]