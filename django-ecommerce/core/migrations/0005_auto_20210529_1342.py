# Generated by Django 2.2 on 2021-05-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('C', 'Clothes'), ('FW', 'Furniture/ Wooden showpieces'), ('EA', 'Ethnic Accessories'), ('O', 'Other items')], max_length=2),
        ),
    ]
