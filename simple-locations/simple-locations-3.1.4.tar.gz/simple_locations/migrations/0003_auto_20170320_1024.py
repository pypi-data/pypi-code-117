# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 01:24
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('simple_locations', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='area',
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
    ]
