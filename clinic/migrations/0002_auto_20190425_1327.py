# Generated by Django 2.1.2 on 2019-04-25 20:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='address_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Ünvanı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='address_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Ünvanı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='description_az',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Klinika Profil Məlumatı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Klinika Profil Məlumatı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='descriptionmeta_az',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Klinika Kard Məlumatı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='descriptionmeta_ru',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Klinika Kard Məlumatı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro1_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 1-ci Metro'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro1_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 1-ci Metro'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro1distance_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='1-ci Metroya olan Məsafə'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro1distance_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='1-ci Metroya olan Məsafə'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro2_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 2-ci Metro'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro2_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 2-ci Metro'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro2distance_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='2-ci Metroya olan Məsafə'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='metro2distance_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='2-ci Metroya olan Məsafə'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='name_az',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Adı'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='name_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Adı'),
        ),
    ]
