# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20150128_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='panty',
            name='description',
            field=models.CharField(default='default description', max_length=300),
            preserve_default=False,
        ),
    ]
