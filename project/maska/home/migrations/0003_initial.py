# Generated by Django 4.2.4 on 2023-08-11 16:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_remove_flight_destination_remove_flight_origen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RoundFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.FloatField(default=6.0)),
                ('travile_time', models.DateField(default=datetime.datetime.now)),
                ('BordingTime', models.FloatField(default=0)),
                ('LandingTime', models.FloatField(default=0)),
                ('Price', models.IntegerField(default=0)),
                ('Returndestination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoundReturnto', to='home.airport')),
                ('Returnorigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoundReturnDepature', to='home.airport')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Roundto', to='home.airport')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RoundDepature', to='home.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.FloatField(default=3.0)),
                ('travile_time', models.DateField(default=datetime.datetime.now)),
                ('BordingTime', models.FloatField(default=0)),
                ('LandingTime', models.FloatField(default=0)),
                ('Price', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='home.airport')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Depature', to='home.airport')),
            ],
        ),
    ]