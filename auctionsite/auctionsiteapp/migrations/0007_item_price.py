# Generated by Django 2.2.6 on 2019-11-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionsiteapp', '0006_auto_20191126_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]