# Generated by Django 4.1 on 2022-09-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0004_alter_truckinterior_number_of_beds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckexterior',
            name='roof_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
