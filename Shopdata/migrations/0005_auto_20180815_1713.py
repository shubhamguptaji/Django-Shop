# Generated by Django 2.1 on 2018-08-15 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shopdata', '0004_auto_20180815_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='categoryName',
            new_name='name',
        ),
    ]