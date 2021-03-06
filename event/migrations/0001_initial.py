# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('image', models.ImageField(blank=True, default='events/images/default.jpg', null=True, upload_to='events/images')),
                ('description', models.TextField(max_length=5000)),
                ('organiser', models.CharField(blank=True, max_length=200, null=True)),
                ('organiser_details', models.TextField(blank=True, null=True, verbose_name=2000)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('price', models.CharField(max_length=100)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('resource', models.FileField(blank=True, default='events/files/default.pdf', null=True, upload_to='events/files')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Country')),
            ],
        ),
        migrations.CreateModel(
            name='EventTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('website', models.URLField()),
                ('image', models.ImageField(blank=True, default='jobs/images/default.jpg', null=True, upload_to='jobs/images')),
                ('resource', models.FileField(blank=True, null=True, upload_to='jobs/files')),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField()),
                ('award_amount', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('website', models.URLField()),
                ('image', models.ImageField(blank=True, default='scholarships/images/default.jpg', null=True, upload_to='scholarships/images')),
                ('resource', models.FileField(blank=True, null=True, upload_to='scholarships/files')),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='scholarship',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.ScholarshipCategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.JobCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventTopic'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventType'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Country'),
        ),
    ]
