# Generated by Django 3.0.6 on 2020-06-30 00:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0020_remove_genericmode_params'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200, unique=True)),
                ('fixed_overhead_per_exposure', models.FloatField(default=1)),
                ('front_padding', models.FloatField(default=90)),
                ('config_change_time', models.FloatField(default=0)),
                ('acquire_exposure_time', models.FloatField(default=0)),
                ('configuration_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=list, size=None)),
                ('default_acceptability_threshold', models.FloatField(default=90.0)),
                ('allow_self_guiding', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='instrument',
            name='science_cameras',
            field=models.ManyToManyField(to='hardware.Camera'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='science_camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='science_camera_for', to='hardware.Camera'),
        ),
        migrations.AddField(
            model_name='genericmodegroup',
            name='instrument_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mode_types', to='hardware.InstrumentType'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='instrument_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hardware.InstrumentType'),
        ),
    ]
