# Generated by Django 2.1.2 on 2019-04-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20190425_1508'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='clinic',
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinics',
            field=models.ManyToManyField(blank=True, null=True, related_name='doctors', through='doctor.ClinicSaatlar', to='clinic.Clinic', verbose_name='İşlədiyi Klinikalar'),
        ),
    ]
