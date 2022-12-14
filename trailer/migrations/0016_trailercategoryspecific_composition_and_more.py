# Generated by Django 4.1 on 2022-09-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0015_alter_trailerdimensions_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailercategoryspecific',
            name='composition',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailercategoryspecific',
            name='logistic_posts',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailercategoryspecific',
            name='scuffliner',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailercategoryspecific',
            name='scuffliner_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailercategoryspecific',
            name='two_speed_landing_gear',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailerchassis',
            name='brake_percent_remaining',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trailerchassis',
            name='skirt_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailerchassis',
            name='skirts',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailerchassis',
            name='tire_percent_remaining',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
