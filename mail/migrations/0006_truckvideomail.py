# Generated by Django 4.1 on 2022-09-09 13:40

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_rename_truck_trailerfriendmail_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckVideoMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('postal_code', models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('^[0-9]{4,6}$', 'Invalid postal code')])),
                ('video_chat_service', models.CharField(max_length=64)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
