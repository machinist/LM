# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-06 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import leerstandsmelder.location.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('building_type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('demolished', models.BooleanField(default=False)),
                ('rumor', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=30)),
                ('empty_since', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=30)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=12)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=12)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=leerstandsmelder.location.models.photo_upload)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location')),
            ],
        ),
    ]
