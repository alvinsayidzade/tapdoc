# Generated by Django 2.1.2 on 2019-04-25 18:09

import ckeditor.fields
import clinic.widgets
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('MRK', 'Merkez'), ('FLL', 'filial')], max_length=25, null=True, verbose_name='Klinika Növü')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Adı')),
                ('address', models.CharField(blank=True, max_length=256, null=True, verbose_name='Klinika Ünvanı')),
                ('phone', models.CharField(blank=True, max_length=256, null=True, verbose_name='Əlaqə Telefonu')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Klinika Profil Məlumatı')),
                ('descriptionmeta', models.TextField(blank=True, max_length=256, null=True, verbose_name='Klinika Kard Məlumatı')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='', verbose_name='Profil Şəkli')),
                ('location', clinic.widgets.LocationField(blank=True, max_length=255, verbose_name='Klinika Xəritədə Yeri')),
                ('be_cm_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='BE - Cümə İş Saatı')),
                ('sn_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='Şənbə İş Saatı')),
                ('bz_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='Bazar İş Saatı')),
                ('metro1', models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 1-ci Metro')),
                ('metro1distance', models.CharField(blank=True, max_length=256, null=True, verbose_name='1-ci Metroya olan Məsafə')),
                ('metro2', models.CharField(blank=True, max_length=256, null=True, verbose_name='Yaxın Olduğu 2-ci Metro')),
                ('metro2distance', models.CharField(blank=True, max_length=256, null=True, verbose_name='2-ci Metroya olan Məsafə')),
            ],
        ),
        migrations.CreateModel(
            name='DiaqnostikalarPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qiymet', models.CharField(blank=True, max_length=64, null=True, verbose_name='Adı')),
                ('diaqnostika', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qiymetler', to='service.Diaqnostikalar', verbose_name='Diaqnpstik Xidmətin Adı')),
                ('klinika', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('star', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('message', models.TextField(blank=True, max_length=4000, null=True)),
                ('published', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinicreviews', to='clinic.Clinic')),
                ('starter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinicreviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sertifikatlar', to='clinic.Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='XidmetlerPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qiymet', models.CharField(blank=True, max_length=64, null=True, verbose_name='Qiymət')),
                ('klinika', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
                ('xidmet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qiymetler', to='service.Xidmatlar', verbose_name='Xidmətin Adı')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='diaqnostikalar',
            field=models.ManyToManyField(blank=True, null=True, related_name='relate_name_diaqnostikalar', through='clinic.DiaqnostikalarPrices', to='service.Diaqnostikalar', verbose_name='Diaqnostik Xidmətlər və qiymətləri'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='filial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filiallar', to='clinic.Clinic', verbose_name='Aid olduğu mərkəz klinika'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='clinicwishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clinic',
            name='xidmetler',
            field=models.ManyToManyField(blank=True, null=True, related_name='relate_name_xidmetler', through='clinic.XidmetlerPrices', to='service.Xidmatlar', verbose_name='Xidmətlər və qiymətləri'),
        ),
    ]
