# Generated by Django 5.1 on 2024-08-25 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0008_remove_user_is_active_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appartments', to='Sknne_app.user'),
        ),
    ]
