# Generated by Django 3.2.6 on 2021-08-31 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_polyline_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='polyline',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
