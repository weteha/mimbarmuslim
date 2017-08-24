# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dalil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('judul', models.CharField(max_length=100)),
                ('isi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('sub_judul', models.CharField(blank=True, max_length=50)),
                ('pemateri', models.CharField(max_length=100)),
                ('tanggal', models.DateField(blank=True)),
                ('waktu_mulai', models.TimeField(blank=True)),
                ('waktu_selesai', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sholat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('waktu', models.CharField(max_length=10)),
                ('hukum', models.CharField(choices=[('wajib', 'wajib'), ('sunnah', 'sunnah')], max_length=10)),
                ('gambar', models.TextField(blank=True)),
            ],
        ),
    ]