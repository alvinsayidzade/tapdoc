# Generated by Django 2.1.2 on 2019-03-03 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_auto_20190303_1412'),
        ('service', '0006_auto_20190303_1423'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Xidmetler',
            new_name='Xidmatlar',
        ),
        migrations.RenameModel(
            old_name='XidmetlerGroup',
            new_name='XidmatlarGroup',
        ),
    ]