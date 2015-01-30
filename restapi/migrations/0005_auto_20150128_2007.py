# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_auto_20150128_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panty',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
