# Generated by Django 5.0.6 on 2024-05-21 00:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('calendar_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('editable_by', models.ManyToManyField(related_name='editable_by', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visible_for', models.ManyToManyField(related_name='visible_for', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(choices=[('AR', 'Arbeit'), ('FR', 'Freizeit')], default='FR', max_length=2)),
                ('calender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_calendar.calendar')),
            ],
        ),
    ]
