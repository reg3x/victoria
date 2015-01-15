# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField(max_length=10)),
                ('picture', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
