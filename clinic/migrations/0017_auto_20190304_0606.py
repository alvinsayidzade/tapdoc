# Generated by Django 2.1.2 on 2019-03-04 14:06

import clinic.widgets
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_auto_20190304_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='longitude',
        ),
        migrations.AddField(
            model_name='clinic',
            name='location',
            field=clinic.widgets.LocationField(blank=True, max_length=255),
        ),
    ]