# Generated by Django 4.2.11 on 2024-05-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('instagram', models.CharField(blank=True, max_length=120)),
                ('linkdin', models.CharField(blank=True, max_length=120)),
                ('tiktok', models.CharField(blank=True, max_length=120)),
                ('x', models.CharField(blank=True, max_length=120)),
                ('born_date', models.DateTimeField()),
                ('born_place', models.CharField(blank=True, max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
