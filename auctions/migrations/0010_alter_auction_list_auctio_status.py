# Generated by Django 4.1 on 2022-08-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_auction_list_auctio_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='auctio_status',
            field=models.BooleanField(default=False),
        ),
    ]
