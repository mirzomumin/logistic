# Generated by Django 4.1 on 2022-09-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0027_truckcategoryspecific_collision_mitigation_system'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='truckimage',
            options={'ordering': ('-image',)},
        ),
        migrations.AlterField(
            model_name='truckimage',
            name='image',
            field=models.ImageField(null=True, upload_to='truck-images/'),
        ),
    ]