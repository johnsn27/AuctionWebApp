# Generated by Django 2.2.6 on 2019-11-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionsiteapp', '0007_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionsiteapp.Item')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionsiteapp.SiteUsers')),
            ],
        ),
    ]
