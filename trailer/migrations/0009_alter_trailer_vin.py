# Generated by Django 4.1 on 2022-09-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0008_alter_trailer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='vin',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
    ]
