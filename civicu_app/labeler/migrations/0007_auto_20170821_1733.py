# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0006_auto_20170804_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date photo was uploaded.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='taken_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Date photo was taken.'),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date photo was changed.'),
        ),
    ]
