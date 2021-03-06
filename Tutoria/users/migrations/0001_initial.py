# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BookingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionTime', models.DateTimeField()),
                ('bookingTime', models.DateTimeField()),
                ('fee', models.IntegerField()),
                ('subject', models.CharField(max_length=8)),
                ('venue', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default='', max_length=100)),
                ('emailAddress', models.EmailField(default='example@example.com', max_length=254)),
                ('phoneNumber', models.CharField(default='', max_length=12)),
                ('walletBalance', models.IntegerField(default=0)),
                ('isStudent', models.BooleanField(default=False)),
                ('isTutor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.UserProfile')),
                ('shortIntro', models.TextField()),
                ('hourlyRate', models.IntegerField()),
                ('blackedOutTime', models.DurationField()),
                ('isContracted', models.BooleanField()),
                ('subjectTag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='timeslot',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tutor'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
        migrations.AddField(
            model_name='bookingrecord',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tutor'),
        ),
        migrations.AddField(
            model_name='blackout',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tutor'),
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
