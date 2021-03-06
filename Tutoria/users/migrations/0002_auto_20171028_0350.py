# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tutor')),
            ],
        ),
        migrations.RemoveField(
            model_name='bookingrecord',
            name='status',
        ),
        migrations.AlterUniqueTogether(
            name='timeslot',
            unique_together=set([('tutor', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='blackout',
            unique_together=set([('tutor', 'date')]),
        ),
    ]
