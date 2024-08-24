# Generated by Django 5.1 on 2024-08-23 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sknne_app', '0006_alter_appartment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appartment',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Sknne_app.appartment')),
            ],
        ),
    ]
