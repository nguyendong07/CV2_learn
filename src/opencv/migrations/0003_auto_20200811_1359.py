# Generated by Django 3.1 on 2020-08-11 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0002_auto_20200810_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='src',
        ),
    ]
