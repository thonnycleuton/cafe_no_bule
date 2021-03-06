# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-10-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name=b'Cantina')),
            ],
            options={
                'verbose_name': 'Cantina',
                'verbose_name_plural': 'Cantinas',
            },
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='cantina',
            field=models.ManyToManyField(blank=True, to='cantina.Cantina'),
        ),
    ]
