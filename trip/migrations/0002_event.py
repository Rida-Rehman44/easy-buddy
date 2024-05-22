# Generated by Django 5.0.6 on 2024-05-21 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='trip.trip')),
            ],
        ),
    ]
