# Generated by Django 3.2.16 on 2022-11-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0023_digitalwallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalwallet',
            name='encrypted_currency',
            field=models.CharField(max_length=1000),
        ),
    ]