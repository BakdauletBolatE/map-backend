# Generated by Django 3.2.6 on 2021-09-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_polyline_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='polyline',
            name='typeMarker',
            field=models.CharField(blank=True, choices=[(1, 'Жол'), (2, 'Су'), (3, 'Кубыр')], max_length=255, null=True),
        ),
    ]
