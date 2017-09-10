# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_upcomingevents_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upcomingevents',
            name='date',
            field=models.DateField(),
        ),
    ]