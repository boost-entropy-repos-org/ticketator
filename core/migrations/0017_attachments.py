# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20160613_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='static/ticket_files/')),
                ('ticket_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ticket')),
            ],
        ),
    ]