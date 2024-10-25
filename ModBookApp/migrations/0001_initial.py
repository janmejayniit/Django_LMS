# Generated by Django 5.1.2 on 2024-10-17 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=240)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages', models.PositiveIntegerField()),
                ('authors', models.TextField(max_length=1500)),
                ('publication', models.TextField(max_length=500)),
                ('isbn', models.TextField(max_length=20)),
                ('edition', models.TextField(max_length=50)),
                ('edition_year', models.TextField(max_length=5)),
                ('description', models.TextField(verbose_name=5000)),
                ('book_conver', models.ImageField(blank=True, null=True, upload_to='book_cover/')),
                ('tags', models.TextField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
