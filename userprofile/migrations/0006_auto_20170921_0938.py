# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-21 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_defaultimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatar_Q7boQrv.png', null=True, upload_to='avatars'),
        ),
    ]
