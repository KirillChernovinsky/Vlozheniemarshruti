# Generated by Django 5.0 on 2023-12-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(verbose_name='Гендер'),
        ),
    ]
