# Generated by Django 4.1 on 2022-09-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0017_trailercategoryspecific_logistic_post_spacing'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailerimage',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='truck-videos'),
        ),
    ]