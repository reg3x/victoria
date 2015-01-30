# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_auto_20150130_1525'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bra',
            new_name='Brasier',
        ),
    ]
