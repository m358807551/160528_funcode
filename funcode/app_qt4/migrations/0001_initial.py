# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mqt4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('solution', models.TextField()),
            ],
        ),
    ]
