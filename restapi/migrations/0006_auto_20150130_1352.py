# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20150128_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bra',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Butter',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cream',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fragance',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Legging',
            fields=[
                ('product_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(max_length=10)),
                ('img', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=50)),
                ('stock', models.IntegerField(max_length=10, verbose_name=b'Cantidad Disponible')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='panty',
            options={'verbose_name_plural': 'panties'},
        ),
    ]
