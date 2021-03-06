# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionTime', models.DateTimeField()),
                ('bookingTime', models.DateTimeField()),
                ('status', models.CharField(max_length=15)),
                ('fee', models.IntegerField()),
                ('subject', models.CharField(max_length=8)),
                ('venue', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContractedTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Tutor',
            },
        ),
        migrations.CreateModel(
            name='PrivateTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Tutor',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('privateTutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PrivateTutor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='cTutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ContractedTutor'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='pTutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PrivateTutor'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
    ]
