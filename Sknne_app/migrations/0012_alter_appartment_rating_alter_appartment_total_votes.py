# Generated by Django 5.1 on 2024-08-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0011_merge_20240829_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appartment',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]
