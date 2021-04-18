# Generated by Django 3.1.7 on 2021-04-18 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=128, verbose_name='address')),
                ('city', models.CharField(default='Almaty', max_length=64, verbose_name='city')),
                ('country', models.CharField(default='Kazakhstan', max_length=64, verbose_name='country')),
                ('zip_code', models.CharField(default='050000', max_length=7, verbose_name='zip code')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
