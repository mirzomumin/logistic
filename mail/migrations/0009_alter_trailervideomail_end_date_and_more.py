# Generated by Django 4.1 on 2022-09-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0008_alter_truckvideomail_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailervideomail',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trailervideomail',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]