# Generated by Django 2.1.2 on 2019-04-26 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
        ('doctor', '0008_auto_20190426_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurancePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packages', models.CharField(blank=True, choices=[('A', 'A Paket'), ('B', 'B Paket'), ('C', 'C Paket')], max_length=25, null=True, verbose_name='Paketler')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hekimler', to='insurance.Company', verbose_name='Company')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='company',
            field=models.ManyToManyField(blank=True, null=True, related_name='doctors', through='doctor.InsurancePackage', to='insurance.Company', verbose_name='İşlədiyi Sığortalar'),
        ),
    ]
