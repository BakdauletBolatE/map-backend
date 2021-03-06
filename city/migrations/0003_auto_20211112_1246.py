# Generated by Django 3.2.8 on 2021-11-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20211112_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='localities',
            name='lat',
            field=models.FloatField(blank=True, default=42.19705782897213, null=True, verbose_name='Лат'),
        ),
        migrations.AddField(
            model_name='localities',
            name='lng',
            field=models.FloatField(blank=True, default=69.95598711561539, null=True, verbose_name='Лат'),
        ),
        migrations.AddField(
            model_name='ruraldistrict',
            name='lat',
            field=models.FloatField(blank=True, default=42.19705782897213, null=True, verbose_name='Лат'),
        ),
        migrations.AddField(
            model_name='ruraldistrict',
            name='lng',
            field=models.FloatField(blank=True, default=69.95598711561539, null=True, verbose_name='Лат'),
        ),
    ]
