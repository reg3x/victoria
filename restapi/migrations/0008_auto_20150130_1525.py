# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_auto_20150130_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bra',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
