# Generated by Django 4.1 on 2022-09-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0003_enginemanufacturer_transmissionmanufacturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckinterior',
            name='number_of_beds',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckinterior',
            name='sleeper_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
