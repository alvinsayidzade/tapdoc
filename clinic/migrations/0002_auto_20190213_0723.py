# Generated by Django 2.1.2 on 2019-02-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='clinic',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
