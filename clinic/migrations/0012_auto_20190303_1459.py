# Generated by Django 2.1.2 on 2019-03-03 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_xidmatlar'),
        ('clinic', '0011_auto_20190303_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='XidmetPrices',
            new_name='Prices',
        ),
    ]