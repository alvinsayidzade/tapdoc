# Generated by Django 2.1.2 on 2019-05-27 11:32

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
        ('insurance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicSaatlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bir_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='1-ci gün İş Saatı')),
                ('iki_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='2-ci gün İş Saatı')),
                ('uc_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='3-ci gün  İş Saatı')),
                ('dord_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='4-ci gün  İş Saatı')),
                ('bes_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='5-ci gün  İş Saatı')),
                ('sn_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='Şənbə İş Saatı')),
                ('bz_issaati', models.CharField(blank=True, max_length=256, null=True, verbose_name='Bazar İş Saatı')),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hekimler', to='clinic.Clinic', verbose_name='Clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Kişi'), ('F', 'Qadın')], max_length=25, null=True, verbose_name='Həkimin Cinsi')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Adı')),
                ('first_name_az', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Adı')),
                ('first_name_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Adı')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Soyadı')),
                ('last_name_az', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Soyadı')),
                ('last_name_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Soyadı')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin titulu')),
                ('title_az', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin titulu')),
                ('title_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin titulu')),
                ('tecrube', models.IntegerField(blank=True, null=True, verbose_name='Həkimin Təcrübəsi')),
                ('contact_phone', models.CharField(blank=True, max_length=256, null=True, verbose_name='Qəbul Üçün Telefon')),
                ('evde_muayine', models.BooleanField(blank=True, null=True, verbose_name='Evdə müayinə')),
                ('evde_muayine_qiymet', models.CharField(blank=True, max_length=256, null=True, verbose_name='Evdə Müayinə Qiyməti')),
                ('evde_muayine_endirim_faiz', models.CharField(blank=True, max_length=256, null=True, verbose_name='Evdə Müayinə Endirim %-lə')),
                ('usaq_hekimi', models.BooleanField(blank=True, null=True, verbose_name='Uşaq həkimi?')),
                ('usaq_hekimi_qiymet', models.CharField(blank=True, max_length=256, null=True, verbose_name='Uşaq Həkimi Müayinə Qiyməti')),
                ('usaq_hekimi_endirim_faiz', models.CharField(blank=True, max_length=256, null=True, verbose_name='Uşaq həkimi Endirim %-lə')),
                ('qebula_yazilma', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkimin Qəbulu Qiyməti')),
                ('qebula_yazilma_endirim_faiz', models.CharField(blank=True, max_length=256, null=True, verbose_name='Həkim Qəbulu Endirim %-lə')),
                ('image', models.ImageField(blank=True, default='defaultdoctor.png', null=True, upload_to='', verbose_name='Profil Şəkli')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Həkim Haqqında Ətraflı Məlumat')),
                ('description_az', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Həkim Haqqında Ətraflı Məlumat')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Həkim Haqqında Ətraflı Məlumat')),
                ('clinics', models.ManyToManyField(blank=True, null=True, related_name='doctors', through='doctor.ClinicSaatlar', to='clinic.Clinic', verbose_name='İşlədiyi Klinikalar')),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hekimler', to='insurance.Company', verbose_name='Company')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='İxtisas adı')),
                ('name_az', models.CharField(blank=True, max_length=256, null=True, verbose_name='İxtisas adı')),
                ('name_ru', models.CharField(blank=True, max_length=256, null=True, verbose_name='İxtisas adı')),
                ('description', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Qısa Məlumat')),
                ('description_az', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Qısa Məlumat')),
                ('description_ru', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Qısa Məlumat')),
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
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='doctor.Doctor')),
                ('starter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sertifikatlar', to='doctor.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='company',
            field=models.ManyToManyField(blank=True, null=True, related_name='doctors', through='doctor.InsurancePackage', to='insurance.Company', verbose_name='İşlədiyi Sığortalar'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='professions',
            field=models.ManyToManyField(blank=True, null=True, related_name='doctors', to='doctor.Profession', verbose_name='Həkimin İxtisasları'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clinicsaatlar',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
