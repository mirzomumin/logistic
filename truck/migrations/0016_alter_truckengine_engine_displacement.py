# Generated by Django 4.1 on 2022-09-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0015_alter_truck_condition_alter_truck_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckengine',
            name='engine_displacement',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
