# Generated by Django 5.1 on 2024-08-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
