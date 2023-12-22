# Generated by Django 4.2.7 on 2023-12-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0006_travel_time_go'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_lname', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_travel_name', models.CharField(max_length=50, verbose_name='Назва туру')),
            ],
        ),
    ]
