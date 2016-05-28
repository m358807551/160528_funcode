# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='question',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='templates',
            name='question',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
