# Generated by Django 2.2.6 on 2019-11-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionsiteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateTimeField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
