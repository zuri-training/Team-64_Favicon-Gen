# Generated by Django 4.1 on 2022-08-03 16:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_generatedfavicon_path_alter_zipfile_path'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ZipFile',
            new_name='FaviconZipFile',
        ),
    ]
