# Generated by Django 4.1 on 2022-09-02 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trailer_utils', '0001_initial'),
        ('trailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trailer_utils.trailercategory'),
        ),
        migrations.AddField(
            model_name='trailer',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trailer_utils.trailermanufacturer'),
        ),
        migrations.AddField(
            model_name='trailer',
            name='qty',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trailer',
            name='state_dot',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='TrailerInterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lining_type', models.CharField(blank=True, max_length=256, null=True)),
                ('trailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trailer.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerExterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doors', models.CharField(blank=True, max_length=256, null=True)),
                ('roof_type', models.CharField(blank=True, max_length=256, null=True)),
                ('insulated', models.CharField(blank=True, max_length=256, null=True)),
                ('lock_rods_number', models.PositiveIntegerField(blank=True, null=True)),
                ('trailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trailer.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerDimensions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('length', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('internal_height', models.PositiveIntegerField(blank=True, null=True)),
                ('trailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trailer.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerChassis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suspension', models.CharField(blank=True, max_length=256, null=True)),
                ('wheels', models.CharField(blank=True, max_length=256, null=True)),
                ('color', models.CharField(blank=True, max_length=256, null=True)),
                ('number_of_rear_axles', models.CharField(blank=True, max_length=256, null=True)),
                ('axle_type', models.CharField(blank=True, max_length=256, null=True)),
                ('floor_type', models.CharField(blank=True, max_length=256, null=True)),
                ('gvw', models.PositiveIntegerField(blank=True, null=True)),
                ('mud_flaps', models.CharField(blank=True, max_length=256, null=True)),
                ('tires', models.DecimalField(decimal_places=1, max_digits=4)),
                ('trailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trailer.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerCategorySpecific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lift_and_gate', models.CharField(blank=True, max_length=256, null=True)),
                ('tariler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trailer.trailer')),
            ],
        ),
    ]
