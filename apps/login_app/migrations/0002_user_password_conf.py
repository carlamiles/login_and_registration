# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-24 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_conf',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
    ]
