# Generated by Django 2.1 on 2018-08-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopdata', '0002_auto_20180815_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='sellerPhoneNumber',
            field=models.CharField(max_length=13),
        ),
    ]
