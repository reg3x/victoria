# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_panty_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panty',
            old_name='picture',
            new_name='img',
        ),
    ]
