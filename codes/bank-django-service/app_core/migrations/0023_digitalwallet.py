# Generated by Django 3.2.16 on 2022-11-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0022_auto_20221127_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('encrypted_currency', models.CharField(max_length=100)),
            ],
        ),
    ]