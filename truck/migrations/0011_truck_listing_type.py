# Generated by Django 4.1 on 2022-09-03 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truck_utils', '0006_listingtype'),
        ('truck', '0010_alter_truckattachments_truck_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='listing_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='truck_utils.listingtype'),
        ),
    ]
