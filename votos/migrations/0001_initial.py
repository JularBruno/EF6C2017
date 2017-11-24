# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-24 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('partido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128, verbose_name='Nombre del distrito')),
                ('cantidad_votantes', models.IntegerField(default=0, verbose_name='Cantidad de votantes')),
                ('latitude', models.DecimalField(decimal_places=10, default=0, max_digits=14, verbose_name='Latitud')),
                ('longitude', models.DecimalField(decimal_places=10, default=0, max_digits=14, verbose_name='Longitud')),
            ],
        ),
        migrations.CreateModel(
            name='Votos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.Candidato')),
                ('distrito_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.Distrito')),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='distrito_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votos.Distrito'),
        ),
    ]
