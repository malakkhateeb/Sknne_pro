# Generated by Django 5.1 on 2024-08-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0005_remove_appartment_room_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
