# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plus', '0002_auto_20160505_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentialsmodel',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
