# Generated by Django 2.1 on 2018-08-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='sellerPhoneNumber',
            field=models.IntegerField(default=0),
        ),
    ]
