# Generated by Django 5.0.9 on 2024-10-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModBookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
