# Generated by Django 5.1 on 2024-08-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0003_merge_20240827_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.FileField(upload_to='static/appartments/images'),
        ),
    ]
