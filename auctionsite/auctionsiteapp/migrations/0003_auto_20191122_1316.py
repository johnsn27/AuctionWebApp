# Generated by Django 2.2.6 on 2019-11-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctionsiteapp', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='SiteUsers',
        ),
    ]